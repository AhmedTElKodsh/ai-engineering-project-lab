"""Negative controls for supplied-source provenance and development-only fixtures."""

import hashlib
from copy import deepcopy

import pytest


@pytest.fixture
def supplied_fixture(tmp_path):
    source = tmp_path / "source.md"
    source.write_text("A supported policy fact.\n", encoding="utf-8")
    corpus = {
        "classification": "supplied_synthetic_development_fixture",
        "fixture_id": "synthetic-pilot",
        "reference_date": "2026-09-24",
        "trusted_context": {"role": "employee", "region": "Cairo"},
        "records": [
            {
                "id": "passage-1",
                "source_path": "source.md",
                "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                "text": "A supported policy fact.",
                "effective_from": "2026-01-01",
                "effective_to": None,
                "status": "active",
                "allowed_roles": ["employee"],
                "regions": ["all"],
            }
        ],
    }
    cases = {
        "classification": "exposed_development_cases_not_independent_assessment",
        "fixture_id": "synthetic-pilot",
        "cases": [{"id": "dev-1", "gold_evidence_ids": ["passage-1"], "expected_status": "answer"}],
    }
    return tmp_path, corpus, cases


def test_retained_source_fixture_is_usable(supplied_fixture):
    from scripts.check_s0_readiness import validate_fixture

    root, corpus, cases = supplied_fixture
    validate_fixture(root, corpus, cases)


@pytest.mark.parametrize(
    "field,value",
    [
        ("source_path", "../secret.md"),
        ("source_sha256", "0" * 64),
        ("text", "An invented extra rule."),
        ("allowed_roles", ["hr_staff"]),
        ("effective_from", "2027-01-01"),
    ],
)
def test_bad_or_ineligible_source_fails_closed(supplied_fixture, field, value):
    from scripts.check_s0_readiness import validate_fixture

    root, corpus, cases = supplied_fixture
    invalid = deepcopy(corpus)
    invalid["records"][0][field] = value
    with pytest.raises(ValueError):
        validate_fixture(root, invalid, cases)


def test_development_case_must_resolve_its_evidence(supplied_fixture):
    from scripts.check_s0_readiness import validate_fixture

    root, corpus, cases = supplied_fixture
    cases["cases"][0]["gold_evidence_ids"] = ["invented-source"]
    with pytest.raises(ValueError):
        validate_fixture(root, corpus, cases)


def test_supplied_answers_cannot_be_labeled_unseen(supplied_fixture):
    from scripts.check_s0_readiness import validate_fixture

    root, corpus, cases = supplied_fixture
    cases["classification"] = "unseen-transfer"
    with pytest.raises(ValueError):
        validate_fixture(root, corpus, cases)
