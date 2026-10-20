"""Route-neutral learning history and derived resume views; no provider or learner code runs."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tempfile
from contextlib import contextmanager
from datetime import UTC, datetime, timedelta
from pathlib import Path

KINDS = {"context", "focus", "execution", "explanation", "transfer", "retention", "correction"}
ASSISTANCE = {"none", "docs", "hints", "worked", "generated", "not_applicable"}
INDEPENDENT = {"none", "docs"}


def contained(root: Path, value: str) -> Path:
    if not isinstance(value, str) or not value or "\\" in value or ":" in value:
        raise ValueError("artifact must be a portable relative path")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError("artifact escapes repository")
    resolved = (root / path).resolve()
    if not resolved.is_relative_to(root.resolve()) or not resolved.is_file():
        raise ValueError("artifact missing or outside repository")
    return resolved


def timestamp(value: str) -> datetime:
    if not isinstance(value, str):
        raise TypeError("timestamp must be text")
    try:
        result = datetime.fromisoformat(value)
    except ValueError as exc:
        raise ValueError("invalid timestamp") from exc
    if result.utcoffset() is None:
        raise ValueError("timestamp requires timezone")
    return result.astimezone(UTC)


def load(root: Path) -> tuple[dict, list[dict], str]:
    route_raw = (root / "learning/route.json").read_bytes()
    route = json.loads(route_raw.decode("utf-8"))
    raw = (root / "learning/evidence.jsonl").read_bytes()
    events = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
    validate(root, route, events)
    contracts = json.dumps(route["_contract_hashes"], sort_keys=True).encode()
    return route, events, hashlib.sha256(route_raw + b"\0" + raw + b"\0" + contracts).hexdigest()


def contract_text(root: Path, path: str, heading: str | None = None) -> str:
    content = contained(root, path).read_text(encoding="utf-8")
    if heading is not None:
        if not isinstance(heading, str) or not heading:
            raise ValueError("invalid contract section")
        match = re.search(rf"(?ms)^{re.escape(heading)}[^\n]*\n.*?(?=^## |\Z)", content)
        if not match:
            raise ValueError("contract section missing")
        content = match.group(0)
    return content


def contract_hash(root: Path, stage: dict) -> str:
    content = contract_text(root, stage["contract"], stage.get("contract_section"))
    for extra in stage.get("additional_contracts", []):
        if isinstance(extra, str):
            content += "\0" + contract_text(root, extra)
        elif isinstance(extra, dict) and set(extra) <= {"path", "section"} and "path" in extra:
            content += "\0" + contract_text(root, extra["path"], extra.get("section"))
        else:
            raise ValueError("invalid additional contract reference")
    facts = {
        "id": stage["id"],
        "requires": stage["requires"],
        "requirements": stage.get("requirements", []),
    }
    if "capabilities" in stage:
        facts["capabilities"] = stage["capabilities"]
    return hashlib.sha256(
        content.encode() + b"\0" + json.dumps(facts, sort_keys=True).encode()
    ).hexdigest()


def validate(root: Path, route: dict, events: list[dict]) -> None:
    if (
        not isinstance(route, dict)
        or type(route.get("schema_version")) is not int
        or route["schema_version"] != 1
    ):
        raise ValueError("invalid route schema")
    stages = route.get("stages")
    if not isinstance(stages, list) or not stages:
        raise ValueError("route requires stages")
    ids: set[str] = set()
    for stage in stages:
        if (
            not isinstance(stage, dict)
            or not isinstance(stage.get("id"), str)
            or not stage["id"].strip()
        ):
            raise ValueError("invalid stage")
        stage_id = stage["id"]
        dependencies = stage.get("requires")
        if stage_id in ids or not isinstance(dependencies, list):
            raise ValueError("duplicate stage or invalid dependencies")
        if any(not isinstance(item, str) or item not in ids for item in dependencies):
            raise ValueError("stage dependencies must precede it")
        hours = stage.get("focused_hours")
        if not isinstance(hours, list) or len(hours) != 2:
            raise ValueError("stage requires hour range")
        if any(type(item) is not int or item < 0 for item in hours) or hours[0] > hours[1]:
            raise ValueError("invalid hour range")
        contained(root, stage["contract"])
        blockers = stage.get("assessment_blockers", [])
        if not isinstance(blockers, list) or any(
            not isinstance(b, str) or not b.strip() for b in blockers
        ):
            raise ValueError("invalid assessment blockers")
        if "capabilities" in stage:
            capabilities = stage["capabilities"]
            if (
                not isinstance(capabilities, list)
                or not capabilities
                or any(not isinstance(c, str) or not c.strip() for c in capabilities)
                or len(set(capabilities)) != len(capabilities)
            ):
                raise ValueError("invalid stage capabilities")
            actions = stage.get("capability_actions", {})
            if (
                not isinstance(actions, dict)
                or set(actions) - set(capabilities)
                or any(not isinstance(a, str) or not a.strip() for a in actions.values())
            ):
                raise ValueError("invalid capability actions")
        ids.add(stage_id)
    route["_contract_hashes"] = {s["id"]: contract_hash(root, s) for s in stages}
    if type(route.get("retention_delay_hours")) is not int or route["retention_delay_hours"] < 24:
        raise ValueError("retention delay must be at least 24 hours")
    contained(root, route["project"] + "/README.md")
    known: dict[str, dict] = {}
    previous = datetime.min.replace(tzinfo=UTC)
    required = {
        "id",
        "at",
        "actor",
        "kind",
        "stage",
        "result",
        "assistance",
        "case",
        "artifact",
        "note",
    }
    for event in events:
        if not isinstance(event, dict) or not required.issubset(event):
            raise ValueError("event missing required fields")
        if (
            set(event)
            - required
            - {
                "target",
                "tree",
                "artifact_sha256",
                "contract_sha256",
                "capabilities",
                "exposed",
            }
        ):
            raise ValueError("event contains unknown fields")
        for field in required:
            if not isinstance(event[field], str) or not event[field].strip():
                raise ValueError(f"event {field} must be nonblank text")
        if event["id"] in known or event["stage"] not in ids:
            raise ValueError("duplicate event or unknown stage")
        when = timestamp(event["at"])
        if when < previous or when > datetime.now(UTC) + timedelta(minutes=1):
            raise ValueError("event time is out of order or in future")
        previous = when
        if event["kind"] not in KINDS or event["assistance"] not in ASSISTANCE:
            raise ValueError("invalid event kind or assistance")
        if event["actor"] not in {"learner", "maintainer"}:
            raise ValueError("invalid actor")
        if event["result"] not in {"pass", "fail", "observed", "invalidated"}:
            raise ValueError("invalid result")
        if "capabilities" in event:
            capabilities = event["capabilities"]
            declared = next(s for s in stages if s["id"] == event["stage"]).get("capabilities", [])
            if (
                not isinstance(capabilities, list)
                or not capabilities
                or any(not isinstance(c, str) for c in capabilities)
                or len(set(capabilities)) != len(capabilities)
                or (
                    set(capabilities) - set(declared)
                    and event.get("contract_sha256") == route["_contract_hashes"][event["stage"]]
                )
            ):
                raise ValueError("unknown or invalid event capabilities")
        if "exposed" in event and (
            type(event["exposed"]) is not bool
            or event["kind"] not in {"context", "focus"}
            or (
                not event["exposed"]
                and (
                    event["actor"] != "maintainer"
                    or event["assistance"] != "not_applicable"
                    or not (event["case"] == "migration" or event["case"].startswith("navigation:"))
                    or "capabilities" in event
                )
            )
        ):
            raise ValueError("only neutral maintainer navigation may be marked unexposed")
        if event["kind"] not in {"context", "focus", "correction"}:
            if event["actor"] != "learner" or event["result"] not in {"pass", "fail"}:
                raise ValueError("learning proof requires learner pass/fail")
            if event["assistance"] == "not_applicable":
                raise ValueError("learning proof must disclose assistance")
            if not isinstance(event.get("contract_sha256"), str) or not re.fullmatch(
                r"[0-9a-f]{64}", event["contract_sha256"]
            ):
                raise ValueError("learning proof requires observed contract hash")
            stage = next(s for s in stages if s["id"] == event["stage"])
            if (
                stage.get("capabilities")
                and event["contract_sha256"] == route["_contract_hashes"][event["stage"]]
                and "capabilities" not in event
            ):
                raise ValueError("current learning proof requires explicit capability scope")
            if not isinstance(event.get("tree"), str) or not event["tree"].strip():
                raise ValueError("learning proof requires tested tree/config identifier")
        elif event["kind"] in {"context", "focus"} and event["result"] != "observed":
            raise ValueError("context/focus cannot award proof")
        artifact = contained(root, event["artifact"])
        if event["kind"] not in {"context", "focus", "correction"}:
            digest = hashlib.sha256(artifact.read_bytes()).hexdigest()
            if event.get("artifact_sha256") != digest:
                raise ValueError("learning proof artifact hash missing or changed")
        if event["kind"] == "correction":
            target = event.get("target")
            if not isinstance(target, str) or target not in known:
                raise ValueError("correction must target an earlier event")
            if known[target]["kind"] == "correction" or known[target]["stage"] != event["stage"]:
                raise ValueError("invalid correction target scope")
            if event["result"] != "invalidated":
                raise ValueError("correction must invalidate")
            if event["assistance"] != "not_applicable" or "capabilities" in event:
                raise ValueError("correction is neutral; record new supplied help as context")
        elif "target" in event:
            raise ValueError("target is only allowed on correction")
        known[event["id"]] = event


def derive(route: dict, events: list[dict], revision: str) -> dict:
    invalidated = {e["target"] for e in events if e["kind"] == "correction"}
    current = [
        e
        for e in events
        if e["id"] not in invalidated
        and e["kind"] != "correction"
        and (
            e["kind"] in {"context", "focus"}
            or e.get("contract_sha256") == route["_contract_hashes"][e["stage"]]
        )
    ]
    position = {e["id"]: i for i, e in enumerate(current)}
    history_position = {e["id"]: i for i, e in enumerate(events)}

    def exposes_case(e: dict) -> bool:
        """True when an earlier event showed the learner this case, so it cannot be fresh."""
        return e["kind"] in {
            "execution",
            "explanation",
            "transfer",
            "retention",
            "context",
            "focus",
        } and e.get("exposed", True)

    def previously_seen_case(proof: dict) -> bool:
        return any(
            e["stage"] == proof["stage"]
            and exposes_case(e)
            and e["case"] == proof["case"]
            and history_position[e["id"]] < history_position[proof["id"]]
            for e in events
        )

    def qualify(scoped: list[dict]) -> dict:
        proofs = {}
        for kind in ["execution", "explanation", "transfer", "retention"]:
            applicable = [e for e in scoped if e["kind"] == kind]
            last_failure = max(
                (timestamp(e["at"]) for e in applicable if e["result"] == "fail"), default=None
            )
            passing = [
                e
                for e in applicable
                if e["result"] == "pass"
                and (last_failure is None or timestamp(e["at"]) > last_failure)
            ]
            if kind in {"transfer", "retention"}:
                passing = [e for e in passing if e["assistance"] in INDEPENDENT]
            elif kind in {"execution", "explanation"}:
                passing = [e for e in passing if e["assistance"] not in {"worked", "generated"}]
            proofs[kind] = passing[-1] if passing else None
        transfer = proofs["transfer"]
        retention = proofs["retention"]
        prerequisites_proof = [proofs["execution"], proofs["explanation"]]
        failure_positions = [
            position[e["id"]]
            for e in scoped
            if e["kind"] in {"execution", "explanation", "transfer"} and e["result"] == "fail"
        ]
        if transfer and (
            any(not p for p in prerequisites_proof)
            or previously_seen_case(transfer)
            or any(
                transfer["case"] == p["case"]
                or transfer["tree"] != p["tree"]
                or position[transfer["id"]] <= position[p["id"]]
                for p in prerequisites_proof
                if p
            )
            or any(position[transfer["id"]] <= i for i in failure_positions)
        ):
            proofs["transfer"] = transfer = None
        if retention and (
            not transfer
            or previously_seen_case(retention)
            or retention["case"] in {p["case"] for p in [*prerequisites_proof, transfer] if p}
            or retention["tree"] != transfer["tree"]
            or timestamp(retention["at"]) - timestamp(transfer["at"])
            < timedelta(hours=route["retention_delay_hours"])
        ):
            proofs["retention"] = None
        return {
            "ready": all(proofs[k] for k in ["execution", "explanation", "transfer"]),
            "retained": all(proofs.values()),
            "proofs": {kind: e["id"] if e else None for kind, e in proofs.items()},
        }

    result = {}
    retention_reviews = []
    for stage in route["stages"]:
        stage_id = stage["id"]
        scoped = [e for e in current if e["stage"] == stage_id]
        aggregate = qualify(scoped)
        capabilities = {
            cap: qualify([e for e in scoped if cap in e.get("capabilities", [])])
            for cap in stage.get("capabilities", [])
        }
        own_ready = (
            all(c["ready"] for c in capabilities.values()) if capabilities else aggregate["ready"]
        )
        own_retained = (
            all(c["retained"] for c in capabilities.values())
            if capabilities
            else aggregate["retained"]
        )
        prerequisites = all(result[item]["ready"] for item in stage["requires"])
        ready = bool(own_ready and prerequisites and not stage.get("assessment_blockers"))
        retained = bool(
            ready and own_retained and all(result[item]["retained"] for item in stage["requires"])
        )
        result[stage_id] = {
            "ready": ready,
            "retained": retained,
            "status": "retained"
            if retained
            else "ready_retention_pending"
            if ready
            else "practicing"
            if scoped and any(e["kind"] not in {"context", "focus"} for e in scoped)
            else "not_started",
            "proofs": aggregate["proofs"],
            "assessment_blockers": stage.get("assessment_blockers", []),
        }
        if capabilities:
            result[stage_id]["capabilities"] = capabilities
            result[stage_id]["pending_capabilities"] = [
                cap for cap, data in capabilities.items() if not data["ready"]
            ]
            for cap, data in capabilities.items():
                if data["ready"] and not data["retained"]:
                    transfer = next(e for e in scoped if e["id"] == data["proofs"]["transfer"])
                    retention_reviews.append(
                        {
                            "stage": stage_id,
                            "capability": cap,
                            "transfer": transfer["id"],
                            "not_before": (
                                timestamp(transfer["at"])
                                + timedelta(hours=route["retention_delay_hours"])
                            ).isoformat(),
                        }
                    )
    eligible = [
        s["id"]
        for s in route["stages"]
        if not result[s["id"]]["ready"] and all(result[item]["ready"] for item in s["requires"])
    ]
    requested = next((e["stage"] for e in reversed(current) if e["kind"] == "focus"), None)
    active = requested if requested in eligible else next(iter(eligible), None)
    notes = [e["note"] for e in current if e["kind"] == "context"]
    active_stage = next((s for s in route["stages"] if s["id"] == active), None)
    next_action = "Revisit pending delayed checks, then defend the complete workbench."
    if active_stage:
        pending = result[active].get("pending_capabilities", [])
        next_action = active_stage.get("capability_actions", {}).get(
            pending[0] if pending else "", active_stage["next_action"]
        )
    return {
        "schema_version": 1,
        "revision": revision,
        "contract_hashes": route["_contract_hashes"],
        "active_stage": active,
        "route_complete": all(s["retained"] for s in result.values()),
        "stages": result,
        "context": notes,
        "retention_reviews": retention_reviews,
        "next_action": next_action,
    }


def resume_view(route: dict, state: dict) -> str:
    lines = [
        "# Learning State",
        "",
        "Generated from learning/route.json and learning/evidence.jsonl. Do not edit this view.",
        "",
        "Learner: Ahmed. Pace: 10 hours/week, five two-hour sessions. CPU first.",
        f"Active project: {route['project']}",
        f"Active stage: {state['active_stage'] or 'retention-review'}",
        f"Evidence revision: {state['revision']}",
        "",
        "## Carried-forward context",
        "",
    ]
    lines += [f"- {note}" for note in state["context"]] or ["No context recorded."]
    lines += ["", "## Stage evidence", "", "| Stage | Status |", "|---|---|"]
    lines += [f"| {stage} | {data['status']} |" for stage, data in state["stages"].items()]
    lines += ["", "## Capability evidence", ""]
    for stage, data in state["stages"].items():
        for blocker in data["assessment_blockers"]:
            lines.append(f"- {stage} assessment pending: {blocker}")
        for cap, proof in data.get("capabilities", {}).items():
            status = (
                "retained"
                if proof["retained"]
                else "ready; retention pending"
                if proof["ready"]
                else "unresolved"
            )
            lines.append(f"- {stage} / {cap}: {status}")
    lines += ["", "## Delayed reviews", ""]
    lines += [
        f"- {r['stage']} / {r['capability']}: not before {r['not_before']}; fresh case required."
        for r in state["retention_reviews"]
    ] or ["No delayed review scheduled yet."]
    lines += [
        "",
        "Repository tests, inherited code and maintainer work do not certify learner competence.",
        "",
        "## Next checkpoint",
        "",
        state["next_action"],
        "",
    ]
    return "\n".join(lines)


def atomic_write(path: Path, value: str) -> None:
    descriptor, temporary = tempfile.mkstemp(dir=path.parent, prefix=".state-", suffix=".tmp")
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(value)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


@contextmanager
def writer(root: Path):
    lock = root / "learning/.writer.lock"
    try:
        handle = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as exc:
        raise ValueError(
            "checkpoint writer already active; inspect stale lock before retry"
        ) from exc
    try:
        os.close(handle)
        yield
    finally:
        lock.unlink()


def save_views(root: Path, route: dict, events: list[dict], revision: str) -> dict:
    state = derive(route, events, revision)
    atomic_write(root / "learning/state.json", json.dumps(state, indent=2) + "\n")
    atomic_write(root / "LEARNING.md", resume_view(route, state))
    check_views(root, route, events, revision)
    return state


def check_views(root: Path, route: dict, events: list[dict], revision: str) -> dict:
    expected = derive(route, events, revision)
    actual = json.loads((root / "learning/state.json").read_text(encoding="utf-8"))
    if actual != expected or (root / "LEARNING.md").read_text(encoding="utf-8") != resume_view(
        route, expected
    ):
        raise ValueError("derived views stale; run refresh without altering the evidence log")
    return expected


def append(root: Path, event: dict, expected_revision: str) -> dict:
    with writer(root):
        route, events, revision = load(root)
        check_views(root, route, events, revision)
        if revision != expected_revision:
            raise ValueError("evidence changed since read; reload before checkpoint")
        stage = next((s for s in route["stages"] if s["id"] == event.get("stage")), None)
        if (
            stage
            and stage.get("assessment_blockers")
            and event.get("kind") in {"transfer", "retention"}
        ):
            raise ValueError("assessment blocked; complete and verify the maintainer prerequisites")
        validate(root, route, events + [event])
        # Ledger replacement preserves the entire byte prefix and avoids a torn append.
        ledger = root / "learning/evidence.jsonl"
        raw = ledger.read_bytes()
        if raw and not raw.endswith(b"\n"):
            raise ValueError("ledger requires trailing newline")
        atomic_write(ledger, raw.decode("utf-8") + json.dumps(event, ensure_ascii=False) + "\n")
        route, events, revision = load(root)
        return save_views(root, route, events, revision)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["validate", "status", "refresh", "append"])
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--event", type=Path)
    parser.add_argument("--expected-revision")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.command == "append":
            if args.event is None or not args.expected_revision:
                raise ValueError("append requires --event and --expected-revision")
            state = append(
                root,
                json.loads(contained(root, args.event.as_posix()).read_text(encoding="utf-8")),
                args.expected_revision,
            )
        elif args.command == "refresh":
            with writer(root):
                route, events, revision = load(root)
                state = save_views(root, route, events, revision)
        else:
            route, events, revision = load(root)
            state = check_views(root, route, events, revision)
        print(
            json.dumps(
                state
                if args.command == "status"
                else {
                    "valid": True,
                    "active_stage": state["active_stage"],
                    "revision": state["revision"],
                },
                indent=2,
            )
        )
        return 0
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(f"Learning state error: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
