"""Evidence relationships, ownership, persistence and stale-session regressions."""

import hashlib
import json
from copy import deepcopy
from datetime import UTC, datetime, timedelta
from pathlib import Path
from unittest.mock import patch

import pytest

from scripts.learning_state import (
    append,
    atomic_write,
    check_views,
    derive,
    load,
    save_views,
    validate,
    writer,
)


@pytest.fixture
def lab(tmp_path: Path):
    (tmp_path / "learning").mkdir()
    (tmp_path / "projects/demo").mkdir(parents=True)
    (tmp_path / "projects/demo/README.md").write_text("Demo contract", encoding="utf-8")
    (tmp_path / "proof.txt").write_text("Observed learner artifact", encoding="utf-8")
    route = {
        "schema_version": 1,
        "project": "projects/demo",
        "retention_delay_hours": 24,
        "stages": [
            {
                "id": name,
                "requires": required,
                "focused_hours": [1, 2],
                "contract": "projects/demo/README.md",
                "next_action": "Next behavior",
            }
            for name, required in [("A", []), ("B", ["A"]), ("C", ["A"])]
        ],
    }
    (tmp_path / "learning/route.json").write_text(json.dumps(route), encoding="utf-8")
    (tmp_path / "learning/evidence.jsonl").write_text("", encoding="utf-8")
    loaded, events, revision = load(tmp_path)
    save_views(tmp_path, loaded, events, revision)
    return tmp_path, loaded


def event(kind="execution", stage="A", hours=0, **changes):
    at = datetime.now(UTC) - timedelta(days=7) + timedelta(hours=hours)
    result = {
        "id": f"{stage}-{kind}-{hours}",
        "at": at.isoformat(),
        "actor": "learner",
        "kind": kind,
        "stage": stage,
        "result": "pass",
        "assistance": "none",
        "case": f"fresh-case-{hours}",
        "artifact": "proof.txt",
        "note": "Observed output",
        "tree": "tested-candidate/config-v1",
        "contract_sha256": hashlib.sha256(
            b"Demo contract"
            + b"\0"
            + json.dumps(
                {"id": stage, "requires": [] if stage == "A" else ["A"], "requirements": []},
                sort_keys=True,
            ).encode()
        ).hexdigest(),
        "artifact_sha256": hashlib.sha256(b"Observed learner artifact").hexdigest(),
    }
    result.update(changes)
    return result


def ready(stage="A", offset=0):
    return [
        event(kind, stage, offset + i)
        for i, kind in enumerate(["execution", "explanation", "transfer"])
    ]


def test_maintainer_work_never_becomes_learning_proof(lab):
    root, route = lab
    with pytest.raises(ValueError, match="learner"):
        validate(root, route, [event(actor="maintainer")])


def test_supported_execution_cannot_complete_owned_stage(lab):
    _, route = lab
    events = ready()
    events[0]["assistance"] = "generated"
    assert not derive(route, events, "revision")["stages"]["A"]["ready"]


def test_hinted_transfer_is_practice_not_independence(lab):
    _, route = lab
    events = ready()
    events[-1]["assistance"] = "hints"
    assert not derive(route, events, "revision")["stages"]["A"]["ready"]


def test_generated_explanation_does_not_award_learner_credit(lab):
    _, route = lab
    events = ready()
    events[1]["assistance"] = "generated"
    assert not derive(route, events, "revision")["stages"]["A"]["ready"]


def test_transfer_cannot_reuse_worked_case(lab):
    _, route = lab
    events = ready()
    events[-1]["case"] = events[0]["case"]
    assert not derive(route, events, "revision")["stages"]["A"]["ready"]


def test_transfer_cannot_reuse_older_generated_practice_case(lab):
    _, route = lab
    supplied = event("execution", hours=-1, assistance="generated", case="supplied-answer")
    events = [supplied, *ready()]
    events[-1]["case"] = "supplied-answer"
    assert not derive(route, events, "revision")["stages"]["A"]["ready"]


def practice_note(stage="A", hours=-1, kind="context", **changes):
    """Assisted practice recorded as context, as PROTOCOL.md directs for partial work."""
    fields = {
        "actor": "learner",
        "result": "observed",
        "assistance": "generated",
        "case": "supplied-answer",
        "note": "Tutor supplied the worked answer for this case",
    }
    fields.update(changes)
    return event(kind, stage, hours, **fields)


def test_transfer_cannot_reuse_context_recorded_practice_case(lab):
    root, route = lab
    events = [practice_note(), *ready()]
    events[-1]["case"] = "supplied-answer"
    validate(root, route, events)
    assert not derive(route, events, "revision")["stages"]["A"]["ready"]


def test_retention_cannot_reuse_context_recorded_practice_case(lab):
    root, route = lab
    events = [practice_note(), *ready(), event("retention", hours=27, case="supplied-answer")]
    validate(root, route, events)
    state = derive(route, events, "revision")["stages"]["A"]
    assert state["ready"] and not state["retained"]


def test_invalidated_context_exposure_is_still_remembered(lab):
    _, route = lab
    note = practice_note()
    correction = event(
        "correction",
        hours=-0.5,
        actor="maintainer",
        result="invalidated",
        assistance="not_applicable",
        target=note["id"],
    )
    events = [note, correction, *ready()]
    events[-1]["case"] = "supplied-answer"
    assert not derive(route, events, "revision")["stages"]["A"]["ready"]


def test_neutral_migration_context_does_not_block_fresh_cases(lab):
    root, route = lab
    migration = practice_note(
        actor="maintainer", assistance="not_applicable", case="migration", note="Support notes"
    )
    events = [migration, *ready()]
    validate(root, route, events)
    assert derive(route, events, "revision")["stages"]["A"]["ready"]


def test_context_exposure_is_scoped_to_its_stage(lab):
    _, route = lab
    events = [practice_note(stage="B"), *ready()]
    events[-1]["case"] = "supplied-answer"
    assert derive(route, events, "revision")["stages"]["A"]["ready"]


def test_execution_repair_does_not_recredit_old_transfer_or_retention(lab):
    _, route = lab
    events = ready() + [event("retention", hours=27)]
    assert derive(route, events, "revision")["stages"]["A"]["retained"]
    events += [event("execution", hours=30, result="fail"), event("execution", hours=31)]
    state = derive(route, events, "revision")
    assert not state["stages"]["A"]["ready"] and not state["stages"]["A"]["retained"]


def test_transfer_must_match_observed_candidate_tree(lab):
    _, route = lab
    events = ready()
    events[-1]["tree"] = "other-candidate"
    assert not derive(route, events, "revision")["stages"]["A"]["ready"]


def test_readiness_advances_without_awarding_retention(lab):
    root, route = lab
    events = ready()
    validate(root, route, events)
    state = derive(route, events, "revision")
    assert state["active_stage"] == "B"
    assert state["stages"]["A"]["ready"] and not state["stages"]["A"]["retained"]
    assert not state["route_complete"]


@pytest.mark.parametrize(
    "hours,same_case,assistance", [(3, False, "none"), (27, True, "none"), (27, False, "hints")]
)
def test_retention_requires_elapsed_time_novelty_and_independence(
    lab, hours, same_case, assistance
):
    _, route = lab
    events = ready()
    proof = event("retention", hours=hours, assistance=assistance)
    if same_case:
        proof["case"] = events[-1]["case"]
    assert not derive(route, events + [proof], "revision")["stages"]["A"]["retained"]


def test_valid_delayed_fresh_case_counts(lab):
    root, route = lab
    events = ready() + [event("retention", hours=27, assistance="docs")]
    validate(root, route, events)
    assert derive(route, events, "revision")["stages"]["A"]["retained"]


def test_retention_cannot_reuse_original_demonstration(lab):
    _, route = lab
    events = ready()
    retention = event("retention", hours=27, case=events[0]["case"])
    assert not derive(route, events + [retention], "revision")["stages"]["A"]["retained"]


def test_failure_reopens_only_relevant_kind_and_dependencies(lab):
    _, route = lab
    events = ready() + ready("B", 4) + ready("C", 8)
    failure = event("execution", "B", 12, result="fail")
    state = derive(route, events + [failure], "revision")
    assert state["stages"]["A"]["ready"] and state["stages"]["C"]["ready"]
    assert not state["stages"]["B"]["ready"]
    assert state["stages"]["B"]["proofs"]["explanation"] is not None


def test_correction_targets_one_event_without_erasing_others(lab):
    root, route = lab
    events = ready()
    correction = event(
        "correction",
        hours=4,
        actor="maintainer",
        result="invalidated",
        assistance="not_applicable",
        target=events[0]["id"],
    )
    validate(root, route, events + [correction])
    state = derive(route, events + [correction], "revision")
    assert not state["stages"]["A"]["ready"]
    assert state["stages"]["A"]["proofs"]["explanation"] == events[1]["id"]
    assert (
        events[-1]["kind"] == "transfer"
    )  # History remains, but its prerequisite was invalidated.


def test_missing_correction_target_is_rejected(lab):
    root, route = lab
    with pytest.raises(ValueError, match="earlier"):
        validate(root, route, [event("correction", result="invalidated", target="missing")])


def test_eligible_offline_focus_preserves_pending_other_stage(lab):
    root, route = lab
    focus = event(
        "focus", "C", 3, actor="maintainer", result="observed", assistance="not_applicable"
    )
    events = ready() + [focus]
    validate(root, route, events)
    state = derive(route, events, "revision")
    assert state["active_stage"] == "C" and not state["stages"]["B"]["ready"]


def test_focus_cannot_bypass_unmet_learning_prerequisite(lab):
    _, route = lab
    focus = event("focus", "C", actor="maintainer", result="observed", assistance="not_applicable")
    assert derive(route, [focus], "revision")["active_stage"] == "A"


@pytest.mark.parametrize(
    "changes",
    [
        {"artifact": "../proof.txt"},
        {"artifact": "C:/secret"},
        {"stage": "unknown"},
        {"at": "2026-01-01"},
        {"tree": []},
        {"artifact_sha256": "wrong"},
        {"assistance": True},
    ],
)
def test_malformed_or_escaping_proof_fails_closed(lab, changes):
    root, route = lab
    with pytest.raises(ValueError):
        validate(root, route, [event(**changes)])


def test_event_artifact_edit_is_detected(lab):
    root, route = lab
    proof = event()
    (root / "proof.txt").write_text("Changed observation", encoding="utf-8")
    with pytest.raises(ValueError, match="hash"):
        validate(root, route, [proof])


def test_route_cycle_or_forward_dependency_is_rejected(lab):
    root, route = lab
    invalid = deepcopy(route)
    invalid["stages"][0]["requires"] = ["C"]
    with pytest.raises(ValueError, match="precede"):
        validate(root, invalid, [])


@pytest.mark.parametrize("change", ["bool_version", "blank_id"])
def test_malformed_route_schema_is_rejected(lab, change):
    root, route = lab
    invalid = deepcopy(route)
    if change == "bool_version":
        invalid["schema_version"] = True
    else:
        invalid["stages"][0]["id"] = " "
    with pytest.raises(ValueError):
        validate(root, invalid, [])


def test_contract_change_invalidates_session_and_old_credit(lab):
    root, _ = lab
    _, _, old_revision = load(root)
    for proof in ready():
        _, _, revision = load(root)
        append(root, proof, revision)
    _, _, previous_revision = load(root)
    (root / "projects/demo/README.md").write_text("Changed required contract", encoding="utf-8")
    route, events, changed_revision = load(root)
    assert changed_revision not in {old_revision, previous_revision}
    assert not derive(route, events, changed_revision)["stages"]["A"]["ready"]


def test_append_preserves_prefix_and_updates_verified_views(lab):
    root, _ = lab
    _, _, revision = load(root)
    append(root, event(), revision)
    before = (root / "learning/evidence.jsonl").read_bytes()
    route, events, revision = load(root)
    append(root, event("explanation", hours=1), revision)
    assert (root / "learning/evidence.jsonl").read_bytes().startswith(before)
    route, events, revision = load(root)
    check_views(root, route, events, revision)


def test_stale_checkpoint_rejects_write(lab):
    root, _ = lab
    _, _, old_revision = load(root)
    append(root, event(), old_revision)
    before = (root / "learning/evidence.jsonl").read_bytes()
    with pytest.raises(ValueError, match="changed"):
        append(root, event("explanation", hours=1), old_revision)
    assert (root / "learning/evidence.jsonl").read_bytes() == before


def test_route_edit_also_invalidates_session_revision(lab):
    root, _ = lab
    route, events, old_revision = load(root)
    route["stages"][0]["next_action"] = "New scope"
    (root / "learning/route.json").write_text(json.dumps(route), encoding="utf-8")
    route, events, new_revision = load(root)
    save_views(root, route, events, new_revision)
    with pytest.raises(ValueError, match="changed"):
        append(root, event(), old_revision)


def test_concurrent_writer_refuses_second_session(lab):
    root, _ = lab
    with writer(root), pytest.raises(ValueError, match="already active"), writer(root):
        pytest.fail("Second writer acquired lock")
    assert not (root / "learning/.writer.lock").exists()


def test_interrupted_view_update_fails_closed_and_refresh_recovers(lab):
    root, _ = lab
    _, _, revision = load(root)
    from scripts import learning_state

    original = learning_state.atomic_write

    def interrupted(path, value):
        if path.name == "LEARNING.md":
            raise OSError("simulated interruption")
        original(path, value)

    with (
        patch.object(learning_state, "atomic_write", side_effect=interrupted),
        pytest.raises(OSError),
    ):
        append(root, event(), revision)
    route, events, revision = load(root)
    with pytest.raises(ValueError, match="stale"):
        check_views(root, route, events, revision)
    save_views(root, route, events, revision)
    assert check_views(root, route, events, revision)["stages"]["A"]["proofs"]["execution"]


def test_failed_atomic_replace_keeps_previous_file(lab):
    root, _ = lab
    output = root / "proof.txt"
    original = output.read_bytes()
    with (
        patch("scripts.learning_state.os.replace", side_effect=OSError("failure")),
        pytest.raises(OSError),
    ):
        atomic_write(output, "replacement")
    assert output.read_bytes() == original
    assert not list(root.glob(".state-*.tmp"))


@pytest.mark.parametrize("kind", ["context", "focus"])
@pytest.mark.parametrize("invalidated", [False, True])
@pytest.mark.parametrize("proof_kind", ["transfer", "retention"])
def test_nonproof_exposure_survives_kind_and_correction(lab, kind, invalidated, proof_kind):
    root, route = lab
    supplied = practice_note(kind=kind)
    events = [supplied]
    if invalidated:
        events.append(
            event(
                "correction",
                hours=-0.5,
                actor="maintainer",
                result="invalidated",
                assistance="not_applicable",
                target=supplied["id"],
            )
        )
    events += ready()
    if proof_kind == "transfer":
        events[-1]["case"] = supplied["case"]
    else:
        events.append(event("retention", hours=27, case=supplied["case"]))
    validate(root, route, events)
    state = derive(route, events, "revision")["stages"]["A"]
    assert not state["ready" if proof_kind == "transfer" else "retained"]


def test_neutral_navigation_can_be_explicit_without_concealing_supplied_help(lab):
    root, route = lab
    neutral = practice_note(
        actor="maintainer",
        assistance="not_applicable",
        case="navigation:resume",
        exposed=False,
    )
    validate(root, route, [neutral, *ready()])
    assert derive(route, [neutral, *ready()], "revision")["stages"]["A"]["ready"]
    with pytest.raises(ValueError, match="neutral"):
        validate(root, route, [practice_note(exposed=False)])


def capability_route(lab):
    root, route = lab
    route["stages"][0]["capabilities"] = ["A.sources", "A.trace"]
    route["stages"][0]["capability_actions"] = {
        "A.sources": "Identify a supported fact and its source.",
        "A.trace": "Trace a local evidence path.",
    }
    (root / "learning/route.json").write_text(json.dumps(route), encoding="utf-8")
    route, events, revision = load(root)
    save_views(root, route, events, revision)
    return root, route


def capability_proof(route, kind, hours, capabilities, **changes):
    return event(
        kind,
        hours=hours,
        capabilities=capabilities,
        contract_sha256=route["_contract_hashes"]["A"],
        **changes,
    )


def capability_ready(route, capabilities, offset=0):
    return [
        capability_proof(route, kind, offset + i, capabilities)
        for i, kind in enumerate(["execution", "explanation", "transfer"])
    ]


def test_one_independent_capability_cannot_close_a_multi_capability_stage(lab):
    root, route = capability_route(lab)
    events = capability_ready(route, ["A.sources"])
    events += capability_ready(route, ["A.trace"], 4)
    events[-1]["assistance"] = "hints"
    validate(root, route, events)
    state = derive(route, events, "revision")
    assert state["stages"]["A"]["capabilities"]["A.sources"]["ready"]
    assert not state["stages"]["A"]["ready"]
    assert state["stages"]["A"]["pending_capabilities"] == ["A.trace"]
    assert state["next_action"] == "Trace a local evidence path."


def test_combined_observation_can_cover_each_explicit_capability(lab):
    root, route = capability_route(lab)
    events = capability_ready(route, ["A.sources", "A.trace"])
    validate(root, route, events)
    state = derive(route, events, "revision")
    assert state["stages"]["A"]["ready"]
    assert not state["stages"]["A"]["retained"]
    assert {r["capability"] for r in state["retention_reviews"]} == {"A.sources", "A.trace"}


def test_capability_failure_preserves_other_capability_and_reopens_dependency(lab):
    root, route = capability_route(lab)
    events = capability_ready(route, ["A.sources", "A.trace"])
    events.append(capability_proof(route, "execution", 4, ["A.trace"], result="fail"))
    validate(root, route, events)
    state = derive(route, events, "revision")["stages"]["A"]
    assert state["capabilities"]["A.sources"]["ready"]
    assert not state["capabilities"]["A.trace"]["ready"]
    assert not state["ready"]


def test_old_stage_only_records_do_not_gain_capability_credit(lab):
    _, route = capability_route(lab)
    state = derive(route, ready(), "revision")["stages"]["A"]
    assert not state["ready"]
    assert state["pending_capabilities"] == ["A.sources", "A.trace"]


def test_capability_retention_is_fresh_delayed_and_individual(lab):
    root, route = capability_route(lab)
    events = capability_ready(route, ["A.sources", "A.trace"])
    events.append(capability_proof(route, "retention", 27, ["A.sources"]))
    validate(root, route, events)
    state = derive(route, events, "revision")["stages"]["A"]
    assert state["capabilities"]["A.sources"]["retained"]
    assert not state["capabilities"]["A.trace"]["retained"]
    assert not state["retained"]


def test_unknown_capability_is_rejected(lab):
    root, route = capability_route(lab)
    with pytest.raises(ValueError, match="capabilit"):
        validate(root, route, [capability_proof(route, "execution", 0, ["A.invented"])])


def test_scoped_dependency_changes_only_its_consumers(lab):
    root, route = lab
    shared = root / "shared.md"
    shared.write_text("## Rules\nRequired policy\n## Other\nUnrelated\n", encoding="utf-8")
    route["stages"][0]["additional_contracts"] = [{"path": "shared.md", "section": "## Rules"}]
    validate(root, route, [])
    initial = route["_contract_hashes"].copy()
    shared.write_text("## Rules\nRequired policy\n## Other\nChanged unrelated\n", encoding="utf-8")
    validate(root, route, [])
    assert route["_contract_hashes"] == initial
    shared.write_text("## Rules\nChanged policy\n## Other\nUnrelated\n", encoding="utf-8")
    validate(root, route, [])
    assert route["_contract_hashes"]["A"] != initial["A"]
    assert route["_contract_hashes"]["B"] == initial["B"]


def test_pending_mentor_pilot_blocks_readiness_without_erasing_observations(lab):
    root, route = capability_route(lab)
    route["stages"][0]["assessment_blockers"] = ["P1-B: actual mentor-host pilot pending"]
    validate(root, route, [])
    events = capability_ready(route, ["A.sources", "A.trace"])
    validate(root, route, events)
    state = derive(route, events, "revision")["stages"]["A"]
    assert state["capabilities"]["A.sources"]["ready"]
    assert not state["ready"]
    assert state["assessment_blockers"] == ["P1-B: actual mentor-host pilot pending"]


def test_changed_capability_list_keeps_old_history_without_promoting_it(lab):
    root, route = capability_route(lab)
    events = capability_ready(route, ["A.sources"])
    route["stages"][0]["capabilities"] = ["A.trace"]
    route["stages"][0]["capability_actions"].pop("A.sources")
    validate(root, route, events)
    assert not derive(route, events, "revision")["stages"]["A"]["ready"]


def test_writer_rejects_new_independent_assessment_while_blocked(lab):
    root, route = capability_route(lab)
    route["stages"][0]["assessment_blockers"] = ["Actual host pilot pending"]
    (root / "learning/route.json").write_text(json.dumps(route), encoding="utf-8")
    route, events, revision = load(root)
    save_views(root, route, events, revision)
    before = (root / "learning/evidence.jsonl").read_bytes()
    proof = capability_proof(route, "transfer", 2, ["A.sources"])
    with pytest.raises(ValueError, match="assessment blocked"):
        append(root, proof, revision)
    assert (root / "learning/evidence.jsonl").read_bytes() == before


@pytest.mark.parametrize("kind", ["execution", "explanation", "transfer", "retention"])
def test_current_proof_cannot_hide_failure_by_omitting_capability_scope(lab, kind):
    root, route = capability_route(lab)
    proof = capability_proof(route, kind, 30, ["A.sources"], result="fail")
    del proof["capabilities"]
    with pytest.raises(ValueError, match="capability scope"):
        validate(root, route, [proof])
