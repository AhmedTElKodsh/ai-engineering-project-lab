#!/usr/bin/env python3
"""Validate routes and derive scheduling from explicit learner evidence.

Default resolution is read-only and never activates the candidate project route.
See docs/learning-path/EVIDENCE-PROTOCOL.md for readiness and retention semantics.
--project-root is the from-scratch/ directory (route, LEARNING.md); --curriculum-root is a
checkout of the upstream curriculum whose phases/ the route's lesson stages resolve against.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import date, timedelta
from math import isfinite
from pathlib import Path

LESSON_REF = re.compile(r"^(\d{2})\.(\d{2})(?:-(\d{2})\.(\d{2}))?$")
LESSON_MODES = {"full", "focused", "paired", "repair"}
CATEGORIES = {"attempt", "focused_bridge", "full_completion", "project_gate"}
STATES = {"not_observed", "pending", "failed", "passed"}
DERIVED = {"ready_to_advance", "retained", "closed", "mastered", "state"}
MIN_RETENTION_DAYS = 7
HEX = re.compile(r"^[0-9a-f]+$")


def obj(value, label):
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be an object")
    return value


def nonempty(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")
    return value


def strings(value, label, allow_empty=False):
    if not isinstance(value, list) or (not value and not allow_empty):
        raise ValueError(
            f"{label} must be a {'possibly empty ' if allow_empty else 'non-empty '}list"
        )
    for item in value:
        nonempty(item, label)
    if len(value) != len(set(value)):
        raise ValueError(f"{label} contains duplicate IDs")
    return value


def boolean(value, label):
    if type(value) is not bool:
        raise ValueError(f"{label} must be a boolean")
    return value


def expand_reference(reference):
    match = LESSON_REF.fullmatch(nonempty(reference, "lesson reference"))
    if not match:
        raise ValueError(f"invalid lesson reference: {reference}")
    phase, start = int(match[1]), int(match[2])
    if match[3] is None:
        return [(phase, start)]
    end_phase, end = int(match[3]), int(match[4])
    if phase != end_phase or end < start:
        raise ValueError(f"invalid inclusive lesson range: {reference}")
    return [(phase, lesson) for lesson in range(start, end + 1)]


def one_directory(parent, prefix, reference):
    matches = sorted(p for p in parent.glob(f"{prefix}-*") if p.is_dir())
    if len(matches) != 1:
        raise ValueError(f"{reference} resolved to {len(matches)} directories")
    return matches[0]


def resolve_lesson(root, phase, lesson):
    lid = f"{phase:02d}.{lesson:02d}"
    directory = one_directory(
        one_directory(root / "phases", f"{phase:02d}", lid), f"{lesson:02d}", lid
    )
    docs, quiz = directory / "docs/en.md", directory / "quiz.json"
    if not docs.is_file():
        raise ValueError(f"{lid} is missing docs/en.md")
    return {
        "kind": "lesson",
        "lesson_id": lid,
        "lesson": f"{phase:02d}/{directory.name}",
        "directory": directory.relative_to(root).as_posix(),
        "docs": docs.relative_to(root).as_posix(),
        "quiz": quiz.relative_to(root).as_posix() if quiz.is_file() else None,
    }


def completed_lessons(learning_file):
    """Legacy Markdown rows alone are untrusted; migrate reviewed evidence."""
    if not learning_file.is_file():
        raise ValueError("LEARNING.md is required")
    return set()


def load_route(root, route_path=None):
    path = route_path or root / "route.json"
    if not path.is_file():
        raise ValueError(f"route file does not exist: {path}")
    route = obj(json.loads(path.read_text(encoding="utf-8")), "route")
    progress = root / nonempty(route.get("progress_file", "LEARNING.md"), "progress_file")
    if not progress.is_file():
        raise ValueError("LEARNING.md is required")
    return route, progress


def validate_and_expand(root, route):
    obj(route, "route")
    if type(route.get("schema_version")) is not int or route["schema_version"] not in {1, 2}:
        raise ValueError("supported route schema_version values are 1 and 2")
    pace = obj(route.get("pace_hours_per_week"), "pace_hours_per_week")
    for key in ("minimum", "maximum"):
        if type(pace.get(key)) not in {int, float} or not isfinite(pace[key]) or pace[key] <= 0:
            raise ValueError(f"pace {key} must be positive")
    if pace["maximum"] < pace["minimum"]:
        raise ValueError("pace maximum must be at least minimum")
    milestones = route.get("milestones")
    if not isinstance(milestones, list) or not milestones:
        raise ValueError("milestones must be a non-empty list")
    active_id = nonempty(route.get("active_milestone"), "active_milestone")
    expanded, mids, sids, pids, active = [], set(), set(), set(), []
    for milestone in milestones:
        obj(milestone, "milestone")
        mid = nonempty(milestone.get("id"), "milestone id")
        if mid in mids:
            raise ValueError(f"duplicate milestone ID: {mid}")
        mids.add(mid)
        if milestone.get("status") not in {"active", "queued", "complete"}:
            raise ValueError(f"invalid milestone status: {mid}")
        if milestone["status"] == "active":
            active.append(milestone)
        nonempty(milestone.get("exit_criteria_source"), "exit_criteria_source")
        stages = milestone.get("stages")
        if not isinstance(stages, list) or not stages:
            raise ValueError(f"{mid} needs non-empty stages")
        required_count = 0
        for stage in stages:
            obj(stage, "stage")
            sid = nonempty(stage.get("id"), "stage id")
            if sid in sids:
                raise ValueError(f"duplicate stage ID: {sid}")
            sids.add(sid)
            required = boolean(stage.get("required"), f"{sid}.required")
            required_count += required
            if not required:
                nonempty(stage.get("condition"), f"{sid}.condition")
            mode = nonempty(stage.get("mode"), f"{sid}.mode")
            focus = strings(
                stage.get("focus", []), f"{sid}.focus", mode not in {"focused", "project"}
            )
            shared = {
                "milestone": mid,
                "stage": sid,
                "stage_title": nonempty(stage.get("title"), f"{sid}.title"),
                "required": required,
                "mode": mode,
                "focus": focus,
            }
            kind = stage.get("kind", "lesson")
            if kind == "lesson":
                if mode not in LESSON_MODES or any(
                    k in stage for k in ("project_stage_id", "project_stage_ids", "gate_ids")
                ):
                    raise ValueError(f"unsupported lesson stage: {sid}")
                seen = set()
                for ref in strings(stage.get("lesson_ids"), f"{sid}.lesson_ids"):
                    for phase, lesson in expand_reference(ref):
                        item = resolve_lesson(root, phase, lesson)
                        if item["lesson"] in seen:
                            raise ValueError(f"duplicate lesson in stage {sid}")
                        seen.add(item["lesson"])
                        expanded.append({**item, **shared})
            elif kind == "project":
                if (
                    route["schema_version"] != 2
                    or mode != "project"
                    or "lesson_ids" in stage
                    or "project_stage_ids" in stage
                ):
                    raise ValueError(f"unsupported project stage: {sid}")
                pid = nonempty(stage.get("project_stage_id"), f"{sid}.project_stage_id")
                if pid in pids:
                    raise ValueError(f"duplicate project stage ID: {pid}")
                pids.add(pid)
                gates = strings(stage.get("gate_ids"), f"{sid}.gate_ids")
                advances = strings(stage.get("advancement_gate_ids"), f"{sid}.advancement_gate_ids")
                if not set(advances) <= set(gates):
                    raise ValueError(f"{sid} advancement gates must be required gates")
                if stage.get("evidence_category") != "project_gate":
                    raise ValueError(f"{sid} must use project_gate evidence")
                expanded.append(
                    {
                        **shared,
                        "kind": kind,
                        "project_stage_id": pid,
                        "gate_ids": gates,
                        "advancement_gate_ids": advances,
                        "evidence_category": "project_gate",
                    }
                )
            else:
                raise ValueError(f"unsupported stage kind: {kind}")
        if not required_count:
            raise ValueError(f"{mid} must have at least one required stage")
    if len(active) != 1 or active[0]["id"] != active_id:
        raise ValueError("route must contain exactly one matching active milestone")
    return active[0], expanded


def check_workspace(root, workspace):
    """The learner workspace must exist and be disjoint from the curriculum checkout."""
    path = Path(nonempty(str(workspace), "learner workspace")).resolve()
    if not path.is_dir():
        raise ValueError(f"learner workspace does not exist: {path}")
    if path == root or path.is_relative_to(root) or root.is_relative_to(path):
        raise ValueError(f"learner workspace must be outside the curriculum root: {path}")
    return path


def evidence_reference(workspace, value, label):
    """Bind a check to a workspace file by path, SHA-256 and commit; return the artifact key."""
    if workspace is None:
        raise ValueError(
            f"{label}: a learner workspace is required (route learner_workspace or --workspace)"
        )
    ref = obj(value, label)
    if ref.keys() - {"path", "sha256", "commit"}:
        raise ValueError(
            f"unsupported {label} fields: {sorted(ref.keys() - {'path', 'sha256', 'commit'})}"
        )
    given = Path(nonempty(ref.get("path"), f"{label}.path"))
    full = (given if given.is_absolute() else workspace / given).resolve()
    if not full.is_relative_to(workspace):
        raise ValueError(f"{label}.path must stay inside the learner workspace: {given}")
    if not full.is_file() or full.stat().st_size == 0:
        raise ValueError(
            f"{label}.path must reference an existing non-empty workspace file: {given}"
        )
    digest = nonempty(ref.get("sha256"), f"{label}.sha256")
    if len(digest) != 64 or not HEX.match(digest):
        raise ValueError(f"{label}.sha256 must be 64 lowercase hex characters")
    if hashlib.sha256(full.read_bytes()).hexdigest() != digest:
        raise ValueError(f"{label}.sha256 does not match the artifact content: {given}")
    commit = nonempty(ref.get("commit"), f"{label}.commit")
    if not 7 <= len(commit) <= 40 or not HEX.match(commit):
        raise ValueError(f"{label}.commit must be a 7-40 character lowercase hex commit ID")
    return (full.as_posix(), digest)


def validate_evidence(
    root, data, expanded, workspace=None, today=None, min_retention_days=MIN_RETENTION_DAYS
):
    today = today or date.today()
    workspace = check_workspace(root, workspace) if workspace is not None else None
    minimum = timedelta(days=min_retention_days)
    artifacts = {}
    obj(data, "evidence")
    if type(data.get("schema_version")) is not int or data["schema_version"] != 1:
        raise ValueError("evidence schema_version must be 1")
    records = data.get("records")
    if not isinstance(records, list):
        raise ValueError("evidence records must be a list")
    ids = set()
    lessons = {x["lesson"] for x in expanded if x["kind"] == "lesson"}
    gates = {
        (x["project_stage_id"], g)
        for x in expanded
        if x["kind"] == "project"
        for g in x["gate_ids"]
    }
    focused = {
        (x["lesson"], x["stage"])
        for x in expanded
        if x["kind"] == "lesson" and x["mode"] == "focused"
    }
    subjects = lessons | {x["project_stage_id"] for x in expanded if x["kind"] == "project"}
    for r in records:
        obj(r, "record")
        if DERIVED & r.keys():
            raise ValueError("readiness/retained/closed states are derived, not accepted flags")
        rid = nonempty(r.get("id"), "record id")
        if rid in ids:
            raise ValueError(f"duplicate evidence ID: {rid}")
        ids.add(rid)
        category = r.get("category")
        if category not in CATEGORIES:
            raise ValueError(f"unknown evidence category: {category}")
        subject = nonempty(r.get("subject"), "record subject")
        if subject not in subjects:
            raise ValueError(
                f"unknown evidence subject: {subject}; store off-route detours separately"
            )
        unknown = r.keys() - {
            "id",
            "category",
            "subject",
            "stage",
            "gate_id",
            "completion_eligible",
            "observed_at",
            "execution",
            "explanation",
            "transfer",
            "retention",
            "support",
            "deferred_depth",
        }
        if unknown:
            raise ValueError(f"unsupported evidence fields: {sorted(unknown)}")
        if category == "project_gate" and (subject, r.get("gate_id")) not in gates:
            raise ValueError(f"unknown project gate: {subject}/{r.get('gate_id')}")
        if category == "focused_bridge" and (subject, r.get("stage")) not in focused:
            raise ValueError("focused_bridge must name its exact focused lesson/stage")
        if category == "full_completion":
            if subject not in lessons:
                raise ValueError(f"unknown lesson completion: {subject}")
            boolean(r.get("completion_eligible"), "completion_eligible")
        if category == "attempt":
            continue
        observed = date.fromisoformat(nonempty(r.get("observed_at"), "observed_at"))
        if observed > today:
            raise ValueError(f"{rid}.observed_at is in the future: {observed}")
        scope = (subject, r.get("gate_id"), r.get("stage"))
        for name in ("execution", "explanation", "transfer", "retention"):
            check = obj(r.get(name), f"{rid}.{name}")
            allowed = {"status", "evidence"}
            if name == "transfer":
                allowed |= {"independent", "kind"}
            if name == "retention":
                allowed |= {"due", "task", "checked_at", "independent", "kind"}
            if check.keys() - allowed:
                raise ValueError(
                    f"unsupported {rid}.{name} fields: {sorted(check.keys() - allowed)}"
                )
            if check.get("status") not in STATES:
                raise ValueError(f"invalid {rid}.{name}.status")
            if check["status"] in {"passed", "failed"}:
                key = evidence_reference(workspace, check.get("evidence"), f"{rid}.{name}.evidence")
                if artifacts.setdefault(key, scope) != scope:
                    raise ValueError(
                        f"{rid}.{name}.evidence reuses an artifact cited for another subject/gate: {key[0]}"
                    )
            if name == "transfer" and check["status"] == "passed":
                boolean(check.get("independent"), "transfer.independent")
                if check.get("kind") not in {"implementation", "debug", "trace", "changed_input"}:
                    raise ValueError("unknown transfer kind")
            if name == "retention" and check["status"] in {"pending", "failed"}:
                due = date.fromisoformat(nonempty(check.get("due"), "retention.due"))
                if due < observed + minimum:
                    raise ValueError(
                        f"{rid}.retention.due must be at least {min_retention_days} days after observed_at"
                    )
                nonempty(check.get("task"), "retention.task")
            if name == "retention" and check["status"] == "passed":
                boolean(check.get("independent"), "retention.independent")
                if check.get("kind") not in {"implementation", "debug", "trace", "changed_input"}:
                    raise ValueError("unknown retention kind")
                checked = date.fromisoformat(
                    nonempty(check.get("checked_at"), "retention.checked_at")
                )
                if checked > today:
                    raise ValueError(f"{rid}.retention.checked_at is in the future: {checked}")
                if checked < observed + minimum:
                    raise ValueError(
                        f"retained evidence must be checked at least {min_retention_days} days after the construction date"
                    )
    return records


def load_evidence(root, route, expanded, override=None, workspace=None, today=None):
    path = override or root / nonempty(
        route.get("evidence_file", "docs/learning-path/evidence.json"), "evidence_file"
    )
    if not path.is_file():
        if override is not None or "evidence_file" in route:
            raise ValueError(f"evidence file does not exist: {path}")
        return []
    return validate_evidence(
        root, json.loads(path.read_text(encoding="utf-8")), expanded, workspace, today
    )


def record_state(record, today=None):
    if record is None:
        return {"ready_to_advance": False, "retention": "not_observed", "retained": False}
    transfer = record["transfer"]
    ready = all(record[n]["status"] == "passed" for n in ("execution", "explanation", "transfer"))
    ready = (
        ready
        and transfer.get("independent") is True
        and transfer.get("kind") in {"implementation", "debug"}
    )
    retention = record["retention"]["status"]
    retained = (
        ready
        and retention == "passed"
        and record["retention"].get("independent") is True
        and record["retention"].get("kind") in {"implementation", "debug"}
    )
    due = record["retention"].get("due")
    overdue = bool(today and ready and not retained and due and date.fromisoformat(due) < today)
    state = {
        "ready_to_advance": ready,
        "retention": retention,
        "retained": retained,
        "retention_task": record["retention"].get("task"),
        "retention_due": due,
        "evidence_id": record["id"],
        "retention_overdue": overdue,
    }
    if overdue:
        state["retention_days_overdue"] = (today - date.fromisoformat(due)).days
    return state


def item_state(item, records, today=None):
    if item["kind"] == "project":
        gates = {}
        for gid in item["gate_ids"]:
            matches = [
                r
                for r in records
                if r["category"] == "project_gate"
                and r["subject"] == item["project_stage_id"]
                and r["gate_id"] == gid
            ]
            gates[gid] = record_state(matches[-1] if matches else None, today)
        ready = all(gates[g]["ready_to_advance"] for g in item["advancement_gate_ids"])
        retained = all(g["retained"] for g in gates.values())
        return {
            "ready_to_advance": ready,
            "retained": retained,
            "closed": retained,
            "pending_gates": [g for g, state in gates.items() if not state["ready_to_advance"]],
            "gates": gates,
        }
    matches = [
        r
        for r in records
        if r["subject"] == item["lesson"]
        and (
            (r["category"] == "full_completion" and r["completion_eligible"] is True)
            or (
                item["mode"] == "focused"
                and r["category"] == "focused_bridge"
                and r["stage"] == item["stage"]
            )
        )
    ]
    state = record_state(matches[-1] if matches else None, today)
    return {**state, "closed": state["retained"]}


def overdue_items(state, subject, stage):
    """List overdue delayed checks from a lesson state or a project stage's gates."""
    found = []
    for gate, g in (state.get("gates") or {None: state}).items():
        if g.get("retention_overdue"):
            found.append(
                {
                    "stage": stage,
                    "subject": subject,
                    "gate": gate,
                    "task": g["retention_task"],
                    "due": g["retention_due"],
                    "days_overdue": g["retention_days_overdue"],
                }
            )
    return found


def resolve_next(active, expanded, records, today=None):
    today = today or date.today()
    pending, overdue = [], []
    for item in expanded:
        if item["milestone"] != active["id"] or not item["required"]:
            continue
        state = item_state(item, records, today)
        subject = item.get("project_stage_id", item.get("lesson"))
        overdue += overdue_items(state, subject, item["stage"])
        if not state["ready_to_advance"]:
            return {
                "status": "next",
                **item,
                "evidence_state": state,
                "pending_obligations": pending,
                "overdue_retention": overdue,
            }
        if not state["closed"]:
            pending.append({"stage": item["stage"], "subject": subject, **state})
    return {
        "status": "milestone_ready_retention_or_gates_pending"
        if pending
        else "milestone_requirements_closed",
        "milestone": active["id"],
        "pending_obligations": pending,
        "overdue_retention": overdue,
        "exit_criteria_source": active["exit_criteria_source"],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    parser.add_argument(
        "--curriculum-root", type=Path, help="checkout holding phases/; defaults to --project-root"
    )
    parser.add_argument("--route", type=Path, help="explicit route override; does not activate it")
    parser.add_argument("--evidence", type=Path, help="explicit evidence fixture; no writes")
    parser.add_argument(
        "--workspace",
        type=Path,
        help="learner workspace holding evidence artifacts (outside the curriculum root)",
    )
    parser.add_argument(
        "--today", type=date.fromisoformat, help="override today's date (testing only)"
    )
    parser.add_argument("--validate", action="store_true")
    args = parser.parse_args(argv)
    root = args.project_root.resolve()
    curriculum = args.curriculum_root.resolve() if args.curriculum_root else root
    try:
        route, learning_file = load_route(root, root / args.route if args.route else None)
        active, expanded = validate_and_expand(curriculum, route)
        completed_lessons(learning_file)
        workspace = args.workspace or route.get("learner_workspace")
        records = load_evidence(
            root,
            route,
            expanded,
            root / args.evidence if args.evidence else None,
            workspace,
            args.today,
        )
        if args.validate:
            result = {
                "status": "valid",
                "lesson_counts": {
                    m["id"]: sum(
                        x["milestone"] == m["id"] and x["kind"] == "lesson" for x in expanded
                    )
                    for m in route["milestones"]
                },
                "project_stage_counts": {
                    m["id"]: sum(
                        x["milestone"] == m["id"] and x["kind"] == "project" for x in expanded
                    )
                    for m in route["milestones"]
                },
                "required_gate_ids": [
                    g
                    for x in expanded
                    if x["kind"] == "project" and x["required"]
                    for g in x["gate_ids"]
                ],
                "evidence_records": len(records),
            }
        else:
            result = resolve_next(active, expanded, records, args.today)
        print(json.dumps(result, ensure_ascii=False))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(json.dumps({"status": "error", "error": str(error)}))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
