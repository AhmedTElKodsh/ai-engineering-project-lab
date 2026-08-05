"""Validate the written project-mentor package and progression contract."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def read(relative_path: str) -> str:
    path = ROOT / relative_path
    try:
        return path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        ERRORS.append(f"{relative_path}: cannot read UTF-8 text ({exc})")
        return ""


def require_all(label: str, text: str, phrases: tuple[str, ...]) -> None:
    text = " ".join(text.split())
    for phrase in phrases:
        if " ".join(phrase.split()) not in text:
            ERRORS.append(f"{label}: missing contract text {phrase!r}")


def require_order(label: str, text: str, earlier: str, later: str) -> None:
    text = " ".join(text.split())
    earlier = " ".join(earlier.split())
    later = " ".join(later.split())
    if earlier not in text or later not in text or text.index(earlier) >= text.index(later):
        ERRORS.append(f"{label}: {earlier!r} must precede {later!r}")


def markdown_section(label: str, text: str, heading: str) -> str:
    matches = list(re.finditer(rf"(?ms)^{re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)", text))
    if len(matches) != 1:
        ERRORS.append(f"{label}: expected exactly one {heading!r} section")
        return ""
    return matches[0].group(1)


def read_linked_asset(project_dir: Path, project_text: str, link: str) -> str:
    match = re.search(rf"\[{re.escape(link)}\]\(([^)]+)\)", project_text, re.IGNORECASE)
    if not match:
        ERRORS.append(f"project README: missing {link} link")
        return ""
    path = (project_dir / match.group(1)).resolve()
    if not path.is_relative_to(ROOT):
        ERRORS.append(f"project README: {link} path escapes repository")
        return ""
    try:
        return path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        ERRORS.append(f"project README: cannot read {link} ({exc})")
        return ""


if len(sys.argv) > 2 or not ROOT.is_dir():
    raise SystemExit("usage: check_mentor_contract.py [repository-root]")

skill = read(".agents/skills/project-mentor/SKILL.md")
interface = read(".agents/skills/project-mentor/agents/openai.yaml")
agents = read("AGENTS.md")
learning = read("LEARNING.md")
workflow = read(".github/workflows/checks.yml")

active_match = re.search(r"(?m)^active_project:\s*([^\s#]+)\s*$", learning)
active_project = active_match.group(1) if active_match else ""
project_dir = (ROOT / active_project).resolve()
if not active_project:
    ERRORS.append("LEARNING.md: missing active_project")
    project = ""
elif Path(active_project).is_absolute() or not project_dir.is_relative_to(ROOT):
    ERRORS.append("LEARNING.md: active_project must stay inside the repository")
    project = ""
else:
    project = read(f"{active_project}/README.md")

handbook = read_linked_asset(project_dir, project, "handbook excerpt") if project else ""
cases_text = read_linked_asset(project_dir, project, "evaluation asset") if project else ""

parts = skill.split("---", 2)
if len(parts) != 3 or parts[0].strip():
    ERRORS.append("SKILL.md: missing leading YAML frontmatter")
else:
    keys = [
        line.partition(":")[0].strip()
        for line in parts[1].splitlines()
        if line and not line[0].isspace() and ":" in line
    ]
    if sorted(keys) != ["description", "name"]:
        ERRORS.append("SKILL.md: frontmatter requires one name and one description")
    if not re.search(r"(?m)^name:\s*project-mentor\s*$", parts[1]):
        ERRORS.append("SKILL.md: name must be exactly project-mentor")
    require_all("SKILL.md frontmatter", parts[1], ("Interactive mentor",))

interface_lines = [line for line in interface.splitlines() if line.strip()]
interface_fields: dict[str, str] = {}
if not interface_lines or interface_lines[0].strip() != "interface:":
    ERRORS.append("agents/openai.yaml: expected top-level interface mapping")
else:
    for line in interface_lines[1:]:
        match = re.fullmatch(r'  ([a-z_]+):\s*"([^"]*)"\s*', line)
        if not match or match.group(1) in interface_fields:
            ERRORS.append(f"agents/openai.yaml: invalid or duplicate interface field {line!r}")
            continue
        interface_fields[match.group(1)] = match.group(2).strip()
    expected_fields = {"display_name", "short_description", "default_prompt"}
    if set(interface_fields) != expected_fields or any(
        not value for value in interface_fields.values()
    ):
        ERRORS.append("agents/openai.yaml: interface fields must be present and non-empty")
    if "$project-mentor" not in interface_fields.get("default_prompt", ""):
        ERRORS.append("agents/openai.yaml: default_prompt must invoke $project-mentor")

load_state = markdown_section("SKILL.md", skill, "## 1. Locate and load state")
route = markdown_section("SKILL.md", skill, "## 2. Route the request")
understanding = markdown_section("SKILL.md", skill, "## 3. Establish or repair understanding")
verification = markdown_section("SKILL.md", skill, "## 6. Verify and record")

# Routing contract 1: confusion wins, including when an attempt is present.
require_order(
    "mixed-confusion routing",
    route,
    "**Confusion, including mixed confusion:**",
    "**Submit an attempt or output:**",
)
require_all(
    "mixed-confusion routing",
    route,
    (
        "takes precedence over every other route",
        "Persist only `Support needed`",
        "without grading it",
        "do not record mastery",
    ),
)

# Routing contract 2: refusal reasoning is only the first orientation criterion.
require_all(
    "partial orientation",
    understanding,
    (
        "A correct refusal-risk reason completes only the first criterion",
        "Keep orientation open",
        "show the relevant excerpt",
        "ask the answer-only question",
    ),
)

# Routing contract 3: a supported answer advances only to source identification.
require_all(
    "supported-answer progression",
    understanding,
    (
        "A correct supported answer completes only the second criterion",
        "display the excerpt again",
        "ask only for its source section",
    ),
)

# Routing contract 4: a persisted support need is repaired before normal progression.
require_all(
    "support resume",
    route,
    (
        "**Resume with recorded support:**",
        "repair that need before",
        "the ordinary `Next checkpoint`",
    ),
)

require_all(
    "state loading safety",
    load_state,
    (
        "Reject absolute paths",
        "resolves outside the repository",
        "including through a symlink",
        "never load expected answers before evaluation analysis begins",
    ),
)
require_all(
    "evidence safety",
    understanding,
    (
        "quote the complete evidence needed in the current message",
        "verbatim from the validated active-project source",
        "Never invent, paraphrase, or label a toy example as project evidence",
        "Request one learner output type only",
    ),
)
require_all(
    "state write safety",
    verification,
    (
        "re-read `LEARNING.md`",
        "never overwrite concurrent learner state",
        "If the write or verification fails",
        "do not announce advancement",
    ),
)
require_all(
    "AGENTS.md mentoring contract",
    agents,
    (
        "confusion wins",
        "persist only `Support needed`",
        "display every fact needed in the current message",
        "verbatim from a validated project source",
        "Never invent project evidence",
        "Ask for one learner output only",
        "One correct reason does not complete orientation",
    ),
)

if len(re.findall(r"(?m)^## Next checkpoint\s*$", learning)) != 1:
    ERRORS.append("LEARNING.md: expected exactly one Next checkpoint heading")
for field in ("Checkpoint", "Demonstrated understanding", "Support needed"):
    matches = re.findall(rf"(?m)^- \*\*{re.escape(field)}:\*\*\s+\S.*$", learning)
    if len(matches) != 1:
        ERRORS.append(f"LEARNING.md: expected one non-empty {field} field")

require_all(
    "project orientation",
    project,
    (
        "## Orientation checkpoints",
        "## Learner-owned implementation slices",
        "Complete these in separate learner turns",
        "verbatim [handbook excerpt](data/handbook.md)",
        "provide only the requested",
        "provide only its source section",
        "wrong account, billing, or single sign-on guidance",
        "medical or financial advice",
        "support rework",
        "[evaluation asset](eval/cases.json)",
    ),
)

# ponytail: Project 1 wording is direct; add per-project checks when Project 2 activates.
orientation_body = markdown_section("project README", project, "## Orientation checkpoints")
slice_body = markdown_section("project README", project, "## Learner-owned implementation slices")
require_order(
    "project orientation",
    orientation_body,
    "1. Explain in ordinary language",
    "2. Given a verbatim",
)
require_order(
    "project orientation",
    orientation_body,
    "2. Given a verbatim",
    "3. Given that verbatim",
)

if handbook and not re.search(r"(?m)^##\s+\S", handbook):
    ERRORS.append("handbook excerpt asset: expected at least one section heading")

if cases_text:
    try:
        cases = json.loads(cases_text)
    except json.JSONDecodeError as exc:
        ERRORS.append(f"evaluation asset: malformed JSON ({exc})")
    else:
        required_case_keys = {"id", "question", "section", "answer_contains", "abstained"}
        if not isinstance(cases, list) or len(cases) != 20:
            ERRORS.append("evaluation asset: expected exactly 20 cases")
        elif any(not isinstance(case, dict) or required_case_keys - case.keys() for case in cases):
            ERRORS.append("evaluation asset: case missing required fields")
        elif any(
            not isinstance(case["id"], str)
            or not case["id"].strip()
            or not isinstance(case["question"], str)
            or not case["question"].strip()
            or not (case["section"] is None or isinstance(case["section"], str))
            or not isinstance(case["answer_contains"], list)
            or not all(isinstance(value, str) for value in case["answer_contains"])
            or not isinstance(case["abstained"], bool)
            for case in cases
        ):
            ERRORS.append("evaluation asset: invalid case field type")
        elif len({case["id"] for case in cases}) != len(cases):
            ERRORS.append("evaluation asset: case ids must be unique")

if slice_body:
    named_choices = (
        "Sentence Transformers",
        "FAISS",
        "Pydantic",
        "LangChain",
        "Qdrant",
        "pgvector",
        "Ragas",
        "promptfoo",
        "LangSmith",
        "Langfuse",
        "FastAPI",
        "LiteLLM",
    )
    for name in named_choices:
        if name.casefold() in slice_body.casefold():
            ERRORS.append(f"project README: implementation slices predetermine {name}")

validator_command = "uv run python scripts/check_mentor_contract.py"
workflow_steps = [
    line.strip() for line in workflow.splitlines() if line.strip().startswith("- run:")
]
validator_step = f"- run: {validator_command}"
ruff_step = "- run: uv run ruff check ."
if workflow_steps.count(validator_step) != 1:
    ERRORS.append("checks workflow: expected one blocking mentor contract step")
if "continue-on-error: true" in workflow:
    ERRORS.append("checks workflow: steps must not allow failure")
if ruff_step not in workflow_steps:
    ERRORS.append("checks workflow: missing Ruff step")
elif validator_step in workflow_steps and workflow_steps.index(
    validator_step
) >= workflow_steps.index(ruff_step):
    ERRORS.append("checks workflow: mentor contract step must precede Ruff")

if ERRORS:
    print("project-mentor contract failed:", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)

print("project-mentor package and written contract pass")
