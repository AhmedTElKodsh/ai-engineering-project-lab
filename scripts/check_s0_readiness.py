"""Check S0 materials and provenance offline; never certify tutoring or learner mastery."""

from __future__ import annotations

import hashlib
import json
from datetime import date
from pathlib import Path

if __package__:
    from .learning_state import check_views, contained, load
else:
    from learning_state import check_views, contained, load


def validate_fixture(root: Path, corpus: dict, cases: dict) -> None:
    if corpus.get("classification") != "supplied_synthetic_development_fixture":
        raise ValueError("starter corpus must remain labeled supplied development material")
    if cases.get("classification") != "exposed_development_cases_not_independent_assessment":
        raise ValueError("supplied dev cases cannot be promoted to unseen assessment")
    if cases["fixture_id"] != corpus["fixture_id"]:
        raise ValueError("fixture identity mismatch")
    reference = date.fromisoformat(corpus["reference_date"])
    ids = set()
    for record in corpus["records"]:
        if not isinstance(record["id"], str) or not record["id"].strip() or record["id"] in ids:
            raise ValueError("missing/duplicate passage ID")
        ids.add(record["id"])
        source = contained(root, record["source_path"])
        if hashlib.sha256(source.read_bytes()).hexdigest() != record["source_sha256"]:
            raise ValueError("source hash changed")
        text = record["text"]
        original = source.read_text(encoding="utf-8")
        if not text.strip() or any(part not in original for part in text.split("\n\n")):
            raise ValueError("passage contains text absent from its retained source")
        if (
            record["status"] != "active"
            or date.fromisoformat(record["effective_from"]) > reference
            or (record["effective_to"] and date.fromisoformat(record["effective_to"]) < reference)
            or corpus["trusted_context"]["role"] not in record["allowed_roles"]
            or not ({"all", corpus["trusted_context"]["region"]} & set(record["regions"]))
        ):
            raise ValueError("starter allowlist contains an ineligible source")
    if not ids:
        raise ValueError("empty source fixture")
    case_ids = set()
    for case in cases["cases"]:
        if not case["id"] or case["id"] in case_ids:
            raise ValueError("missing/duplicate development case ID")
        case_ids.add(case["id"])
        if set(case["gold_evidence_ids"]) - ids:
            raise ValueError("development evidence ID is missing")
        if case["expected_status"] not in {"answer", "clarify", "abstain"}:
            raise ValueError("unknown response status")


def check(root: Path) -> dict:
    route, events, revision = load(root)
    state = check_views(root, route, events, revision)
    project = route["project"]
    corpus = json.loads(contained(root, project + "/data/starter-corpus.json").read_text("utf-8"))
    cases = json.loads(contained(root, project + "/eval/starter-dev-cases.json").read_text("utf-8"))
    validate_fixture(root, corpus, cases)
    if len(corpus["records"]) != 9 or len(cases["cases"]) != 12:
        raise ValueError("starter fixture differs from the declared nine-passage/twelve-case scope")
    if "pf-leave-carryover" not in {r["id"] for r in corpus["records"]}:
        raise ValueError("S0 source excerpt missing")
    archive = "archive/planning/2026-10-20/"
    manifest = json.loads(contained(root, archive + "MANIFEST.json").read_text("utf-8-sig"))
    for entry in manifest:
        archived = contained(root, entry["archived"])
        if not archived.is_relative_to((root / archive).resolve()):
            raise ValueError("archive manifest points outside its declared archive")
        if hashlib.sha256(archived.read_bytes()).hexdigest() != entry["sha256"]:
            raise ValueError("archived original bytes changed")
    return {
        "materials_valid": True,
        "active_stage": state["active_stage"],
        "passages": len(corpus["records"]),
        "exposed_dev_cases": len(cases["cases"]),
        "archived_originals_verified": len(manifest),
        "assessment_blockers": state["stages"]["S0"]["assessment_blockers"],
        "claim": "S0 materials ready for supported practice; no tutor/mastery/live proof awarded",
    }


if __name__ == "__main__":
    try:
        print(json.dumps(check(Path(__file__).resolve().parents[1]), indent=2))
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(f"S0 readiness error: {exc}")
        raise SystemExit(1) from exc
