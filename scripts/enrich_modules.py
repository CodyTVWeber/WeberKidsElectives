#!/usr/bin/env python3
"""
Enrich all curriculum foundation module Markdown files by appending
additional, subject-appropriate content while preserving existing structure.

Rules:
- Do not rename files or alter existing headings beyond appending content.
- Only add to existing sections when present (Objectives, Materials, Grammar,
  Logic, Rhetoric, Procedure, Portfolio, Safety, Assessment).
- Be idempotent: running multiple times should not duplicate inserts.
- Preserve indentation/formatting style used in the files (Markdown bullets
  use "- ", procedures use "1) ", etc.).
"""

from __future__ import annotations

import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_GLOBS = [
    REPO_ROOT / "curriculum" / "math" / "foundations" / "modules" / "*.md",
    REPO_ROOT / "curriculum" / "music" / "foundations" / "modules" / "*.md",
    REPO_ROOT / "curriculum" / "mechanics" / "foundations" / "modules" / "*.md",
]


def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def write_text(p: Path, s: str) -> None:
    p.write_text(s, encoding="utf-8")


def subject_for(path: Path) -> str:
    parts = {part.lower() for part in path.parts}
    if "math" in parts:
        return "math"
    if "music" in parts:
        return "music"
    if "mechanics" in parts:
        return "mechanics"
    return "generic"


def compile_patterns() -> dict[str, re.Pattern[str]]:
    return {
        "Objectives": re.compile(r"^####\s+Objectives\s*$"),
        "Materials": re.compile(r"^####\s+Materials(?:\s*\(prep\))?\s*$"),
        "Grammar": re.compile(r"^####\s+Grammar(?:\s*\(vocab\))?\s*$"),
        "Logic": re.compile(r"^####\s+Logic(?:\s+prompts)?\s*$"),
        "Rhetoric": re.compile(r"^####\s+Rhetoric(?:\s*\(share\))?\s*$"),
        "Procedure": re.compile(r"^####\s+Procedure\s*$"),
        "Portfolio": re.compile(r"^####\s+Portfolio\s*$"),
        "Safety": re.compile(r"^####\s+Safety\s*$"),
        "Assessment": re.compile(r"^####\s+Assessment\s*$"),
        "Heading": re.compile(r"^###\s+"),
        "AnySection": re.compile(r"^####\s+"),
    }


PATS = compile_patterns()


def find_section_bounds(lines: list[str], start_idx: int) -> tuple[int, int]:
    """Given the index of a section heading line, return (lo, hi_exclusive)
    covering the section's content lines (not including the heading itself)."""
    lo = start_idx + 1
    hi = len(lines)
    for j in range(lo, len(lines)):
        if PATS["AnySection"].match(lines[j]):
            hi = j
            break
    return lo, hi


def section_indices(lines: list[str], pattern: re.Pattern[str]) -> list[int]:
    return [i for i, line in enumerate(lines) if pattern.match(line)]


def ensure_bullets(lines: list[str], heading_pat: re.Pattern[str], bullets: list[str]) -> bool:
    """Append bullets to the bullet list under the given heading if present.
    Returns True if any change was made."""
    changed = False
    idxs = section_indices(lines, heading_pat)
    if not idxs:
        return False
    for hidx in idxs:
        lo, hi = find_section_bounds(lines, hidx)
        # Determine where the current bullet list ends (consecutive lines starting with "- ")
        last_bullet_idx = None
        for j in range(lo, hi):
            if lines[j].startswith("- "):
                last_bullet_idx = j
            elif lines[j].strip() == "":
                # allow a single blank inside list; continue
                continue
            else:
                break
        if last_bullet_idx is None:
            # no bullets; insert right after heading
            insert_at = lo
        else:
            insert_at = last_bullet_idx + 1

        # Avoid duplicates by checking presence
        for b in bullets:
            if any(b.strip() == lines[k].strip()[2:] if lines[k].startswith("- ") else False for k in range(lo, hi)):
                continue
            lines.insert(insert_at, f"- {b}")
            insert_at += 1
            hi += 1
            changed = True
    return changed


def determine_procedure_style(proc_lines: list[str]) -> tuple[str, int]:
    """Return (delim, last_number), where delim is ")" or "." and last_number is
    the highest existing step number. Defaults to (")", 0) if none found."""
    step_re = re.compile(r"^(\d+)([\).])\s")
    last = 0
    delim = ")"
    for line in proc_lines:
        m = step_re.match(line)
        if m:
            num = int(m.group(1))
            last = max(last, num)
            delim = m.group(2)
    return delim, last


def ensure_procedure_steps(lines: list[str], new_steps: list[str]) -> bool:
    changed = False
    idxs = section_indices(lines, PATS["Procedure"])
    if not idxs:
        return False
    for hidx in idxs:
        lo, hi = find_section_bounds(lines, hidx)
        delim, last = determine_procedure_style(lines[lo:hi])
        # Avoid duplicates by checking if any new step text already present
        existing_block = "\n".join(lines[lo:hi])
        insert_at = hi
        to_add: list[str] = []
        n = last
        for s in new_steps:
            if s in existing_block:
                continue
            n += 1
            to_add.append(f"{n}{delim} {s}")
        if to_add:
            # Insert just before hi (which is next heading), preserving a possible trailing blank line
            trailing_blank = (hi - 1 >= lo) and lines[hi - 1].strip() == ""
            if trailing_blank:
                insert_at = hi - 1
            for step in to_add:
                lines.insert(insert_at, step)
                insert_at += 1
            changed = True
    return changed


def enrichment_for(subject: str) -> dict[str, list[str]]:
    if subject == "math":
        return {
            "Objectives": [
                "Use multiple representations (ten‑frames, number lines, equations) to model thinking",
                "Justify strategy choice and compare efficiency with a partner",
            ],
            "Materials": [
                "Number line strips; dry‑erase markers; small sticky notes",
            ],
            "Grammar": [
                "Equation", "Representation", "Efficient",
            ],
            "Logic": [
                "When might a number line be clearer than a ten‑frame?",
                "How can you check if an answer is reasonable?",
            ],
            "Rhetoric": [
                "Record a 20‑second explanation of one problem for your portfolio",
            ],
            "Procedure": [
                "Guided practice: 3 mixed problems with think‑aloud (8–10 min)",
                "Independent practice: 4–6 problems with choice of model (10–12 min)",
                "Reflection: choose one problem and explain your strategy (3–5 min)",
            ],
            "Portfolio": [
                "Attach the reflection sentence and highlight the representation used",
            ],
            "Safety": [
                "Keep floors clear of small pieces; store manipulatives neatly",
            ],
        }
    if subject == "music":
        return {
            "Objectives": [
                "Maintain posture and tall vowels throughout phrases",
                "Self‑monitor breath marks and dynamics; adjust in real time",
            ],
            "Materials": [
                "Pencil for score marks; metronome app or device",
            ],
            "Grammar": [
                "Posture", "Dynamics", "Phrase shape",
            ],
            "Logic": [
                "How does lighter volume help tuning when singing a round?",
                "Where is the best place to breathe in this phrase and why?",
            ],
            "Rhetoric": [
                "Perform for a peer/family member and describe one improvement",
            ],
            "Procedure": [
                "Solfege or tone warm‑up aligned to the piece (3–5 min)",
                "Targeted drill: 2 tricky measures on a neutral syllable (5–7 min)",
                "Run‑through with dynamic plan, then debrief (5–8 min)",
            ],
            "Portfolio": [
                "Circle the most in‑tune measure; write one breath or vowel goal",
            ],
            "Safety": [
                "Use moderate volume; rest voice between repetitions",
            ],
        }
    if subject == "mechanics":
        return {
            "Objectives": [
                "Sketch and label parts with arrows showing motion/force flow",
                "Compare two designs for trade‑offs (speed, torque, complexity)",
            ],
            "Materials": [
                "Ruler or calipers; painter’s tape for labels; safety glasses as needed",
            ],
            "Grammar": [
                "Input", "Output", "Trade‑off", "Tolerance",
            ],
            "Logic": [
                "What changes if you double the gear ratio or lever arm?",
                "How do you ensure parts go back in the correct order?",
            ],
            "Rhetoric": [
                "Explain your build or teardown to a visitor using the notebook",
            ],
            "Procedure": [
                "Plan: predict outcome/ratio and note in notebook (5–7 min)",
                "Test: run trial, record observations and measurements (8–10 min)",
                "Iterate: make one change and compare results (8–10 min)",
            ],
            "Portfolio": [
                "Add a labeled diagram with arrows; include one quantitative measurement",
            ],
            "Safety": [
                "Wear eye protection when appropriate; no loose hair/jewelry near moving parts",
            ],
        }
    # Fallback (should not be used in this repo)
    return {
        "Objectives": ["Explain reasoning to a partner", "Reflect on next steps"],
        "Materials": ["Timer; pencil; sticky notes"],
        "Grammar": ["Model", "Reflect"],
        "Logic": ["What strategy works best here?"],
        "Rhetoric": ["Share a brief explanation with an audience"],
        "Procedure": [
            "Guided practice with feedback (8–10 min)",
            "Independent practice (8–10 min)",
            "Reflection and share (3–5 min)",
        ],
        "Portfolio": ["Add a short reflection sentence"],
        "Safety": ["Keep workspace tidy and materials organized"],
    }


def enrich_file(path: Path) -> bool:
    if path.name.lower() == "readme.md":
        return False
    text = read_text(path)
    if "<!-- enriched: v1 -->" in text:
        return False  # already enriched
    lines = text.splitlines()
    subj = subject_for(path)
    enrich = enrichment_for(subj)

    changed = False
    changed |= ensure_bullets(lines, PATS["Objectives"], enrich["Objectives"])
    changed |= ensure_bullets(lines, PATS["Materials"], enrich["Materials"])
    changed |= ensure_bullets(lines, PATS["Grammar"], enrich["Grammar"])
    changed |= ensure_bullets(lines, PATS["Logic"], enrich["Logic"])
    changed |= ensure_bullets(lines, PATS["Rhetoric"], enrich["Rhetoric"])
    changed |= ensure_procedure_steps(lines, enrich["Procedure"])
    changed |= ensure_bullets(lines, PATS["Portfolio"], enrich["Portfolio"])
    changed |= ensure_bullets(lines, PATS["Safety"], enrich["Safety"])

    if not changed:
        return False

    # Append marker to ensure idempotency
    # Ensure file ends with a single newline before marker
    if lines and lines[-1].strip() != "":
        lines.append("")
    lines.append("<!-- enriched: v1 -->")
    lines.append("")
    write_text(path, "\n".join(lines))
    return True


def main() -> int:
    module_files: list[Path] = []
    for g in MODULE_GLOBS:
        # Expand each absolute pattern by globbing in its parent
        module_files.extend(sorted(g.parent.glob(g.name)))

    if not module_files:
        print("[warn] No module files found to enrich.")
        return 0

    changed_count = 0
    for p in module_files:
        try:
            if enrich_file(p):
                changed_count += 1
                print(f"[ok] enriched: {p}")
        except Exception as exc:  # noqa: BLE001
            print(f"[skip] {p}: {exc}")

    print(f"[done] Enrichment complete. Files changed: {changed_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

