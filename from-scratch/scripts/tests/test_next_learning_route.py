"""Read-only scheduling contracts; synthetic evidence lives in temporary fixtures."""

import contextlib
import copy
import hashlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CURRICULUM = (
    Path(os.environ["FROM_SCRATCH_CURRICULUM"])
    if os.environ.get("FROM_SCRATCH_CURRICULUM")
    else None
)
spec = importlib.util.spec_from_file_location(
    "learning_route", REPO / "scripts/next_learning_route.py"
)
route_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(route_module)


class RouteTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        base = Path(self.temp.name)
        self.root, self.workspace = base / "curriculum", base / "learner-workspace"
        self.root.mkdir()
        self.workspace.mkdir()
        self.today = date(2026, 10, 25)
        (self.workspace / "proof.md").write_text(
            "Synthetic workspace artifact, not learner evidence.", encoding="utf-8"
        )
        (self.root / "LEARNING.md").write_text(
            "## Progress log\n| Date | Lesson | Quiz | Note |\n", encoding="utf-8"
        )
        (self.root / "proof.md").write_text(
            "Synthetic test artifact, not learner evidence.", encoding="utf-8"
        )
        for slug in ("01-one", "02-two"):
            doc = self.root / "phases/11-llm-engineering" / slug / "docs/en.md"
            doc.parent.mkdir(parents=True)
            doc.write_text("# Test lesson\n", encoding="utf-8")
        self.route = {
            "schema_version": 1,
            "pace_hours_per_week": {"minimum": 5, "maximum": 7},
            "active_milestone": "M1",
            "milestones": [
                {
                    "id": "M1",
                    "status": "active",
                    "exit_criteria_source": "proof.md",
                    "stages": [
                        {
                            "id": "focus",
                            "title": "Focused",
                            "required": True,
                            "mode": "focused",
                            "focus": ["one mechanism"],
                            "lesson_ids": ["11.01"],
                        },
                        {
                            "id": "full",
                            "title": "Full later",
                            "required": True,
                            "mode": "full",
                            "lesson_ids": ["11.01", "11.02"],
                        },
                    ],
                }
            ],
        }
        self.active, self.items = route_module.validate_and_expand(self.root, self.route)

    def ev(self, name="proof.md", commit="abc1234"):
        data = (self.workspace / name).read_bytes()
        return {"path": name, "sha256": hashlib.sha256(data).hexdigest(), "commit": commit}

    def record(self, category="focused_bridge", subject="11/01-one"):
        record = {
            "id": "r1",
            "category": category,
            "subject": subject,
            "observed_at": "2026-10-12",
            "execution": {"status": "passed", "evidence": self.ev()},
            "explanation": {"status": "passed", "evidence": self.ev()},
            "transfer": {
                "status": "passed",
                "evidence": self.ev(),
                "independent": True,
                "kind": "implementation",
            },
            "retention": {
                "status": "pending",
                "due": "2026-10-20",
                "task": "Fresh independent change",
            },
        }
        if category == "focused_bridge":
            record["stage"] = "focus"
        if category == "full_completion":
            record["completion_eligible"] = True
        if category == "project_gate":
            record["gate_id"] = "G0"
        return record

    def validate_records(self, records, items=None):
        return route_module.validate_evidence(
            self.root,
            {"schema_version": 1, "records": records},
            items or self.items,
            self.workspace,
            self.today,
        )

    def test_empty_evidence_schedules_first_required(self):
        self.assertEqual(
            route_module.resolve_next(self.active, self.items, [], self.today)["stage"], "focus"
        )

    def test_focused_bridge_advances_scope_but_not_later_full(self):
        records = self.validate_records([self.record()])
        result = route_module.resolve_next(self.active, self.items, records)
        self.assertEqual(result["stage"], "full")
        self.assertEqual(result["lesson"], "11/01-one")
        self.assertFalse(result["pending_obligations"][0]["retained"])

    def test_eligible_full_can_satisfy_focus_and_full(self):
        records = self.validate_records([self.record("full_completion")])
        self.assertEqual(
            route_module.resolve_next(self.active, self.items, records)["lesson"], "11/02-two"
        )

    def test_ineligible_full_does_not_advance(self):
        record = self.record("full_completion")
        record["completion_eligible"] = False
        self.assertEqual(
            route_module.resolve_next(self.active, self.items, self.validate_records([record]))[
                "stage"
            ],
            "focus",
        )

    def test_attempt_presence_does_not_advance(self):
        records = self.validate_records(
            [{"id": "attempt", "category": "attempt", "subject": "11/01-one"}]
        )
        self.assertFalse(route_module.item_state(self.items[0], records)["ready_to_advance"])

    def test_changed_input_is_not_construction(self):
        record = self.record()
        record["transfer"]["kind"] = "changed_input"
        self.assertFalse(
            route_module.record_state(self.validate_records([record])[0])["ready_to_advance"]
        )

    def test_assisted_transfer_does_not_advance(self):
        record = self.record()
        record["transfer"]["independent"] = False
        self.assertFalse(
            route_module.record_state(self.validate_records([record])[0])["ready_to_advance"]
        )

    def test_failed_retention_preserves_readiness_with_targeted_obligation(self):
        record = self.record()
        record["retention"].update(status="failed", evidence=self.ev())
        state = route_module.record_state(self.validate_records([record])[0])
        self.assertTrue(state["ready_to_advance"])
        self.assertFalse(state["retained"])
        self.assertEqual(state["retention"], "failed")
        self.assertEqual(state["retention_task"], "Fresh independent change")

    def test_retained_requires_delayed_pass(self):
        record = self.record()
        record["retention"] = {
            "status": "passed",
            "evidence": self.ev(),
            "checked_at": "2026-10-20",
            "independent": True,
            "kind": "debug",
        }
        self.assertTrue(route_module.record_state(self.validate_records([record])[0])["retained"])

    def test_forged_readiness_flags_rejected(self):
        for key in ("ready_to_advance", "retained", "closed", "mastered", "state"):
            with self.subTest(key=key), self.assertRaises(ValueError):
                record = self.record()
                record[key] = True
                self.validate_records([record])

    def test_missing_evidence_reference_rejected(self):
        record = self.record()
        record["execution"]["evidence"] = {**self.ev(), "path": "missing.md"}
        with self.assertRaises(ValueError):
            self.validate_records([record])

    def test_string_independent_flag_rejected(self):
        record = self.record()
        record["transfer"]["independent"] = "true"
        with self.assertRaises(ValueError):
            self.validate_records([record])

    def test_duplicate_evidence_ids_rejected(self):
        with self.assertRaises(ValueError):
            self.validate_records([self.record(), self.record()])

    def test_wrong_focused_scope_rejected(self):
        record = self.record()
        record["stage"] = "full"
        with self.assertRaises(ValueError):
            self.validate_records([record])

    def test_boolean_string_rejected(self):
        for key, value in (("required", "false"), ("required", 1), ("mode", "invented")):
            with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                bad = copy.deepcopy(self.route)
                bad["milestones"][0]["stages"][0][key] = value
                route_module.validate_and_expand(self.root, bad)

    def test_empty_required_stage_rejected(self):
        bad = copy.deepcopy(self.route)
        bad["milestones"][0]["stages"][0]["lesson_ids"] = []
        with self.assertRaises(ValueError):
            route_module.validate_and_expand(self.root, bad)

    def test_unsupported_project_field_cannot_disappear(self):
        bad = copy.deepcopy(self.route)
        stage = bad["milestones"][0]["stages"][0]
        del stage["lesson_ids"]
        stage["project_stage_ids"] = ["S0"]
        with self.assertRaises(ValueError):
            route_module.validate_and_expand(self.root, bad)

    def test_duplicate_milestone_and_stage_ids_rejected(self):
        for mode in ("milestone", "stage", "overlapping_range"):
            with self.subTest(mode=mode), self.assertRaises(ValueError):
                bad = copy.deepcopy(self.route)
                if mode == "milestone":
                    bad["milestones"].append(copy.deepcopy(bad["milestones"][0]))
                elif mode == "stage":
                    bad["milestones"][0]["stages"][1]["id"] = "focus"
                else:
                    bad["milestones"][0]["stages"][1]["lesson_ids"] = ["11.01-11.02", "11.02"]
                route_module.validate_and_expand(self.root, bad)

    def test_unknown_kind_rejected(self):
        bad = copy.deepcopy(self.route)
        bad["milestones"][0]["stages"][0]["kind"] = "surprise"
        with self.assertRaises(ValueError):
            route_module.validate_and_expand(self.root, bad)

    def test_legacy_failed_or_focused_row_untrusted(self):
        (self.root / "LEARNING.md").write_text(
            "## Progress log\n| d | 11/01-one | 0/2 | focused; deferred |\n", encoding="utf-8"
        )
        self.assertEqual(route_module.completed_lessons(self.root / "LEARNING.md"), set())

    def test_candidate_has_all_nine_stages_and_s0_next(self):
        candidate = json.loads((REPO / "route.json").read_text(encoding="utf-8"))
        active, items = route_module.validate_and_expand(self.root, candidate)
        self.assertEqual([x["project_stage_id"] for x in items], [f"S{i}" for i in range(9)])
        self.assertTrue(all(x["required"] for x in items))
        self.assertEqual(route_module.resolve_next(active, items, [])["project_stage_id"], "S0")
        self.assertEqual(candidate["pace_hours_per_week"], {"minimum": 10, "maximum": 10})

    def test_live_gates_pending_while_local_stage_advances(self):
        candidate = json.loads((REPO / "route.json").read_text(encoding="utf-8"))
        _, items = route_module.validate_and_expand(self.root, candidate)
        record = self.record("project_gate", "S2")
        record["gate_id"] = "G2"
        records = self.validate_records([record], items)
        state = route_module.item_state(items[2], records)
        self.assertTrue(state["ready_to_advance"])
        self.assertFalse(state["closed"])
        self.assertEqual(state["pending_gates"], ["S2-live-generation", "S2-semantic-retrieval"])

    @unittest.skipUnless(
        CURRICULUM, "set FROM_SCRATCH_CURRICULUM to an upstream curriculum checkout"
    )
    def test_superseded_m1_route_still_selects_1101(self):
        route, _ = route_module.load_route(REPO, REPO / "route.m1-superseded.json")
        active, items = route_module.validate_and_expand(CURRICULUM, route)
        self.assertEqual(route_module.resolve_next(active, items, [])["lesson_id"], "11.01")
        self.assertEqual(route["pace_hours_per_week"], {"minimum": 5, "maximum": 7})

    def test_cli_malformed_route_reports_json_error(self):
        bad = self.root / "bad.json"
        bad.write_text('{"schema_version":1,"milestones":null}', encoding="utf-8")
        result = subprocess.run(
            [
                sys.executable,
                str(REPO / "scripts/next_learning_route.py"),
                "--project-root",
                str(self.root),
                "--route",
                str(bad),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout)["status"], "error")

    def test_unknown_attempt_subject_rejected(self):
        with self.assertRaises(ValueError):
            self.validate_records([{"id": "a", "category": "attempt", "subject": "unknown/detour"}])

    def test_same_day_retention_rejected(self):
        record = self.record()
        record["retention"] = {
            "status": "passed",
            "evidence": self.ev(),
            "checked_at": "2026-10-12",
            "independent": True,
            "kind": "debug",
        }
        with self.assertRaises(ValueError):
            self.validate_records([record])

    def test_completion_eligible_must_be_boolean(self):
        record = self.record("full_completion")
        record["completion_eligible"] = "true"
        with self.assertRaises(ValueError):
            self.validate_records([record])

    def test_unknown_derived_flag_rejected(self):
        record = self.record()
        record["readiness"] = "approved"
        with self.assertRaises(ValueError):
            self.validate_records([record])

    def test_assisted_or_changed_input_retention_does_not_establish_retained(self):
        for independent, kind in (
            (False, "implementation"),
            (True, "changed_input"),
            (True, "trace"),
        ):
            with self.subTest(independent=independent, kind=kind):
                record = self.record()
                record["retention"] = {
                    "status": "passed",
                    "evidence": self.ev(),
                    "checked_at": "2026-10-20",
                    "independent": independent,
                    "kind": kind,
                }
                state = route_module.record_state(self.validate_records([record])[0])
                self.assertTrue(state["ready_to_advance"])
                self.assertFalse(state["retained"])

    def test_retention_independent_string_and_nested_flags_rejected(self):
        record = self.record()
        record["retention"] = {
            "status": "passed",
            "evidence": self.ev(),
            "checked_at": "2026-10-20",
            "independent": "true",
            "kind": "debug",
        }
        with self.assertRaises(ValueError):
            self.validate_records([record])
        record = self.record()
        record["execution"]["ready_to_advance"] = True
        with self.assertRaises(ValueError):
            self.validate_records([record])

    def forged_gate_records(self, evidence):
        candidate = json.loads((REPO / "route.json").read_text(encoding="utf-8"))
        _, items = route_module.validate_and_expand(self.root, candidate)
        records = []
        for item in items:
            for n, gate in enumerate(item["gate_ids"]):
                record = self.record("project_gate", item["project_stage_id"])
                record.update(id=f"forged-{item['project_stage_id']}-{n}", gate_id=gate)
                for name in ("execution", "explanation", "transfer"):
                    record[name]["evidence"] = evidence
                records.append(record)
        return items, records

    def test_forged_readme_in_curriculum_root_rejected(self):
        (self.root / "README.md").write_text("forged", encoding="utf-8")
        data = (self.root / "README.md").read_bytes()
        items, records = self.forged_gate_records(
            {
                "path": str(self.root / "README.md"),
                "sha256": hashlib.sha256(data).hexdigest(),
                "commit": "abc1234",
            }
        )
        self.assertEqual(len(records), 13)
        with self.assertRaisesRegex(ValueError, "inside the learner workspace"):
            self.validate_records(records, items)

    def test_forged_probe_through_cli_returns_error(self):
        (self.root / "README.md").write_text("forged", encoding="utf-8")
        shutil.copy(REPO / "route.json", self.root / "route.json")
        _items, records = self.forged_gate_records(
            {"path": "README.md", "sha256": "0" * 64, "commit": "abc1234"}
        )
        (self.root / "evidence.json").write_text(
            json.dumps({"schema_version": 1, "records": records}), encoding="utf-8"
        )
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = route_module.main(
                [
                    "--project-root",
                    str(self.root),
                    "--route",
                    "route.json",
                    "--evidence",
                    "evidence.json",
                    "--workspace",
                    str(self.workspace),
                    "--today",
                    "2026-10-25",
                ]
            )
        self.assertEqual(code, 1)
        self.assertEqual(json.loads(out.getvalue())["status"], "error")

    def test_one_workspace_artifact_cannot_certify_many_gates(self):
        items, records = self.forged_gate_records(self.ev())
        with self.assertRaisesRegex(ValueError, "reuses an artifact"):
            self.validate_records(records, items)

    def test_workspace_required_and_must_be_outside_root(self):
        data = {"schema_version": 1, "records": [self.record()]}
        with self.assertRaisesRegex(ValueError, "workspace is required"):
            route_module.validate_evidence(self.root, data, self.items, None, self.today)
        with self.assertRaisesRegex(ValueError, "outside the curriculum root"):
            route_module.validate_evidence(self.root, data, self.items, self.root, self.today)
        with self.assertRaisesRegex(ValueError, "outside the curriculum root"):
            route_module.validate_evidence(
                self.root, data, self.items, self.root.parent, self.today
            )

    def test_hash_mismatch_and_path_escape_rejected(self):
        record = self.record()
        record["execution"]["evidence"] = {**self.ev(), "sha256": "f" * 64}
        with self.assertRaisesRegex(ValueError, "does not match"):
            self.validate_records([record])
        (self.root / "outside.md").write_text("x", encoding="utf-8")
        record = self.record()
        record["execution"]["evidence"] = {**self.ev(), "path": "../curriculum/outside.md"}
        with self.assertRaisesRegex(ValueError, "inside the learner workspace"):
            self.validate_records([record])

    def test_commit_required_and_string_evidence_rejected(self):
        record = self.record()
        record["execution"]["evidence"] = {**self.ev(), "commit": "not-a-commit"}
        with self.assertRaises(ValueError):
            self.validate_records([record])
        record = self.record()
        record["execution"]["evidence"] = "proof.md"
        with self.assertRaises(ValueError):
            self.validate_records([record])

    def test_future_dates_rejected(self):
        record = self.record()
        record["observed_at"] = "2026-10-26"
        with self.assertRaisesRegex(ValueError, "future"):
            self.validate_records([record])
        record = self.record()
        record["retention"] = {
            "status": "passed",
            "evidence": self.ev(),
            "checked_at": "2026-10-26",
            "independent": True,
            "kind": "debug",
        }
        with self.assertRaisesRegex(ValueError, "future"):
            self.validate_records([record])

    def test_minimum_retention_delay_enforced(self):
        record = self.record()
        record["retention"] = {
            "status": "passed",
            "evidence": self.ev(),
            "checked_at": "2026-10-18",
            "independent": True,
            "kind": "debug",
        }
        with self.assertRaisesRegex(ValueError, "at least 7 days"):
            self.validate_records([record])
        record = self.record()
        record["retention"]["due"] = "2026-10-15"
        with self.assertRaisesRegex(ValueError, "at least 7 days"):
            self.validate_records([record])

    def test_overdue_retention_reported(self):
        records = self.validate_records([self.record()])
        late = route_module.resolve_next(self.active, self.items, records, date(2026, 10, 25))
        self.assertEqual(late["overdue_retention"][0]["days_overdue"], 5)
        self.assertTrue(late["pending_obligations"][0]["retention_overdue"])
        early = route_module.resolve_next(self.active, self.items, records, date(2026, 10, 20))
        self.assertEqual(early["overdue_retention"], [])


if __name__ == "__main__":
    unittest.main()
