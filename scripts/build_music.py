#!/usr/bin/env python3
"""
Compose a single progression-focused Music curriculum Markdown (and optional PDF) from nested files.

- Removes time references
- Adds suggested age notes
"""

from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path


def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def write_text(p: Path, s: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")


def strip_time(line: str) -> str:
    line = re.sub(r"\((?:\d+\s*[–-]\s*\d+|\d+)\s*(?:min|mins|minutes?|h|hrs?|hours?)\)", "", line, flags=re.I)
    return re.sub(r"\s{2,}", " ", line).rstrip()


def transform_module(md: str, ages: str) -> str:
    out: list[str] = []
    added_age = False
    for raw in md.splitlines():
        line = raw
        if not added_age and line.startswith("### "):
            out.append(line)
            out.append(f"Suggested ages: {ages}")
            added_age = True
            continue
        if line.strip().startswith("Use:"):
            continue
        if line.strip().lower().startswith("see also"):
            continue
        line = strip_time(line)
        out.append(line)
    return "\n".join(out).strip() + "\n\n"


def build_progression(root: Path) -> Path:
    music_dir = root / "curriculum" / "music"
    build_dir = root / "build"
    build_dir.mkdir(exist_ok=True)

    parts: list[str] = []
    parts.append("\n".join([
        "# Music/Singing curriculum: progression (ages 3–10)",
        "", "This document is composed from the nested music curriculum. Time references are removed.",
        "Use suggested ages as guidance and move at your pace.", "" ]))

    # Resources
    resources = music_dir / "resources.md"
    if resources.exists():
        parts.append("## Resources and props\n\n" + read_text(resources).strip() + "\n\n")

    # Foundations
    parts.append("## Foundations (suggested ages 3–7)\n\n")
    modules_dir = music_dir / "foundations" / "modules"
    for md_path in sorted(modules_dir.glob("*.md")):
        if md_path.name.lower() == "readme.md":
            continue
        parts.append(transform_module(read_text(md_path), ages="3–7"))

    # Syllabus (as outline beyond modules)
    syllabus = music_dir / "foundations" / "syllabus.md"
    if syllabus.exists():
        parts.append("## Outline\n\n" + read_text(syllabus).strip() + "\n\n")

    out_md = build_dir / "music-progression.md"
    write_text(out_md, "\n".join(parts).strip() + "\n")
    return out_md


def maybe_pdf(md_path: Path) -> None:
    if not shutil.which("pandoc"):
        print("[info] pandoc not found; skipping PDF generation")
        return
    pdf = md_path.with_suffix(".pdf")
    try:
        subprocess.run(["pandoc", str(md_path), "-o", str(pdf), "--from=gfm", "-V", "geometry:margin=1in"], check=True)
        print(f"[ok] Wrote {pdf}")
    except subprocess.CalledProcessError as exc:
        print(f"[warn] pandoc failed: {exc}")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    md = build_progression(root)
    print(f"[ok] Wrote {md}")
    maybe_pdf(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

