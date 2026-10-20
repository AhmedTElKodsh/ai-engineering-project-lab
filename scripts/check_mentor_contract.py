"""Structural package health; does not certify tutor behavior or learner competence."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from learning_state import check_views, load


def check(root: Path) -> list[str]:
    errors = []
    required = [
        "README.md",
        "AGENTS.md",
        "project-context.md",
        "LEARNING.md",
        "TOOLING.md",
        "learning/PROTOCOL.md",
        "docs/teaching/AUTHORING.md",
        "docs/learning-path/02-PROJECT-ROADMAP.md",
        "scripts/check_s0_readiness.py",
        ".agents/skills/project-mentor/SKILL.md",
        ".agents/skills/project-mentor/agents/openai.yaml",
    ]
    for relative in required:
        if not (root / relative).is_file():
            errors.append(f"Missing {relative}")
    try:
        route, events, revision = load(root)
        check_views(root, route, events, revision)
        expected = [f"S{i}" for i in range(7)]
        if [s["id"] for s in route["stages"]] != expected:
            errors.append("Workbench route must contain the declared S0–S6 stages")
        if any(not s.get("capabilities") for s in route["stages"]):
            errors.append("Every stage must declare its critical capabilities")
        if list((root / "docs/learning-path").glob("*.md")) != [
            root / "docs/learning-path/02-PROJECT-ROADMAP.md"
        ]:
            errors.append("Exactly one active detailed plan is required")
        if (
            route["weekly_hours"],
            route["sessions_per_week"],
            route["session_hours"],
            route["compute"],
        ) != (10, 5, 2, "cpu"):
            errors.append("Route disagrees with confirmed pace/compute")
    except (OSError, ValueError, TypeError, KeyError) as exc:
        errors.append(f"Learning state: {exc}")
    skills = list((root / ".agents/skills").glob("*/SKILL.md"))
    if [p.parent.name for p in skills] != ["project-mentor"]:
        errors.append("Exactly one active mentor is required")
    for path in root.rglob("*.md"):
        relative = path.relative_to(root)
        if any(p.startswith(".") for p in relative.parts) and relative.parts[0] != ".agents":
            continue
        if (
            relative.parts[0] == "archive"
            or relative.parts[:3] == ("docs", "review", "independent")
            or relative.parts[:2] == ("resources", "from-scratch-lessons")
        ):
            continue  # Frozen reports and verbatim upstream lessons are not maintained paths.
        text = path.read_text(encoding="utf-8")
        inside = False
        prose = []
        for line, value in enumerate(text.splitlines(), 1):
            if value.startswith("```"):
                if not inside and not value[3:].strip():
                    errors.append(f"{relative}:{line}: untagged code fence")
                inside = not inside
            elif not inside:
                prose.append(value)
        if inside:
            errors.append(f"{relative}: unclosed code fence")
        for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", "\n".join(prose)):
            target = target.strip().strip("<>")
            if urlsplit(target).scheme or target.startswith("#"):
                if re.match(r"^[A-Za-z]:[/\\]", target):
                    errors.append(f"{relative}: machine-specific link")
                continue
            link = (path.parent / unquote(target.split("#", 1)[0])).resolve()
            if not link.is_relative_to(root.resolve()) or not link.exists():
                errors.append(f"{relative}: missing/escaping link {target}")
    for name, count in [("cases.json", 20), ("challenges.json", 4)]:
        path = root / "projects/grounded_support_assistant/eval" / name
        try:
            cases = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(cases, list) or len(cases) != count:
                raise ValueError("unexpected case count")
            if len({c["id"] for c in cases}) != count:
                raise ValueError("duplicate case ID")
            for case in cases:
                if (
                    not isinstance(case["question"], str)
                    or not case["question"].strip()
                    or type(case["abstained"]) is not bool
                ):
                    raise ValueError("malformed question/expected abstention")
        except (ValueError, OSError, KeyError, TypeError) as exc:
            errors.append(f"{name}: {exc}")
    for lab in sorted((root / "resources/labs").iterdir()):
        if not lab.is_dir():
            continue
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "--collect-only", str(lab / "tests"), "-q"],
            cwd=root,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=30,
            check=False,
        )
        if result.returncode:
            errors.append(
                f"{lab.name}: exercise collection failed: {result.stdout[-500:]} {result.stderr[-500:]}"
            )
    return errors


if __name__ == "__main__":
    root = (
        Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else Path(__file__).resolve().parents[1]
    )
    try:
        errors = check(root)
    except (ValueError, OSError, subprocess.TimeoutExpired) as exc:
        errors = [str(exc)]
    if errors:
        print("Package validation failed:\n" + "\n".join(errors))
        raise SystemExit(1)
    print("Package/state/active links and six exercise collections pass.")
    print(
        "Structural proof only; learner behavior, live APIs and retained competence are unverified."
    )
