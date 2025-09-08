#!/usr/bin/env python3
"""
Build a single progression-focused Markdown (and optional PDF) from the nested curriculum.

- Removes week/year time references in composed output
- Adds suggested age ranges where appropriate
"""

from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path


def read_text(file_path: Path) -> str:
    return file_path.read_text(encoding="utf-8")


def write_text(file_path: Path, content: str) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding="utf-8")


def strip_time_references(line: str) -> str:
    # Remove parenthetical time ranges like (10 min), (15–20 min), (2 hours)
    line = re.sub(r"\((?:\d+\s*[–-]\s*\d+|\d+)\s*(?:min|mins|minutes?|h|hrs?|hours?)\)", "", line, flags=re.IGNORECASE)
    # Remove extra double spaces left behind
    line = re.sub(r"\s{2,}", " ", line).rstrip()
    return line


def transform_week_content(md: str, suggested_ages: str) -> str:
    lines = md.splitlines()
    out_lines: list[str] = []
    heading_handled = False
    week_heading_pattern = re.compile(r"^(#+)\s+Week\s+\d+\s+[—-]\s*(.+)$")
    procedure_heading_pattern = re.compile(r"^(#+\s+Procedure)\s*\([^)]*\)\s*$", re.IGNORECASE)
    for line in lines:
        m = week_heading_pattern.match(line.strip())
        if m and not heading_handled:
            # Replace heading, insert suggested ages line after it
            out_lines.append(f"{m.group(1)} {m.group(2)}")
            out_lines.append(f"Suggested ages: {suggested_ages}")
            heading_handled = True
            continue
        # Normalize Procedure heading by removing time annotation
        p = procedure_heading_pattern.match(line.strip())
        if p:
            out_lines.append(p.group(1))
            continue
        # Drop template file path references in compiled doc
        if line.strip().startswith("Use:"):
            continue
        # Drop cross-file pointers
        if line.strip().startswith("See also:"):
            continue
        # Replace references like "Week 5" or "Weeks 2–9" with "earlier work"
        line = re.sub(r"Weeks?\s+\d+(?:\s*[–-]\s*\d+)?", "earlier work", line)
        # Strip inline time references
        line = strip_time_references(line)
        out_lines.append(line)
    return "\n".join(out_lines).strip() + "\n\n"


def transform_years_outline(md: str) -> str:
    # Rename header
    md = re.sub(
        r"^###\s+Years\s+2–6\s+outline.*$",
        "### Progression beyond foundations",
        md,
        flags=re.MULTILINE,
    )
    # Convert "#### Year N (7–8): Title" → "#### Progression stage: Title (suggested ages 7–8)"
    md = re.sub(
        r"^####\s+Year\s+\d+\s+\(([^)]+)\):\s*(.+)$",
        r"#### Progression stage: \2 (suggested ages \1)",
        md,
        flags=re.MULTILINE,
    )
    return md.strip() + "\n\n"


def build_progression(root: Path) -> Path:
    curriculum_dir = root / "curriculum"
    build_dir = root / "build"
    build_dir.mkdir(exist_ok=True)

    parts: list[str] = []

    # Title and how-to
    parts.append(
        "\n".join(
            [
                "# Mechanics curriculum: progression (ages 6–16)",
                "",
                "This single document is composed from the nested curriculum, with time references removed.",
                "Use age ranges as guidance and proceed at your learner’s pace.",
                "",
            ]
        )
    )

    # Safety first
    safety_path = curriculum_dir / "safety.md"
    if safety_path.exists():
        safety_md = read_text(safety_path)
        # Convert Year-based bullets to age-based phrases in safety progression
        safety_md = re.sub(r"^-\s*Year\s*1:\s*", "- Suggested ages 6–7: ", safety_md, flags=re.MULTILINE)
        safety_md = re.sub(r"^-\s*Years\s*2[–-]3:\s*", "- Suggested ages 7–9: ", safety_md, flags=re.MULTILINE)
        safety_md = re.sub(r"^-\s*Years\s*4[–-]6:\s*", "- Suggested ages 9–14: ", safety_md, flags=re.MULTILINE)
        safety_md = re.sub(r"^-\s*Years\s*7\+:\s*", "- Suggested ages 14+: ", safety_md, flags=re.MULTILINE)
        parts.append("## Safety guide\n\n" + safety_md.strip() + "\n\n")

    # Resources
    resources_path = curriculum_dir / "resources.md"
    if resources_path.exists():
        parts.append("## Resources and kits\n\n" + read_text(resources_path).strip() + "\n\n")

    # Foundations lessons (Year 1 weeks → Stage: Foundations ages 6–7)
    weeks_dir = curriculum_dir / "year-1" / "weeks"
    if weeks_dir.exists():
        parts.append("## Foundations (suggested ages 6–7)\n\n")
        for week_file in sorted(weeks_dir.glob("week-*.md")):
            transformed = transform_week_content(read_text(week_file), suggested_ages="6–7")
            parts.append(transformed)

    # Progression beyond foundations (Years 2–6 outline)
    outline_path = curriculum_dir / "years-2-6-outline.md"
    if outline_path.exists():
        parts.append(transform_years_outline(read_text(outline_path)))

    # Write Markdown
    output_md = build_dir / "progression.md"
    write_text(output_md, "\n".join(parts).strip() + "\n")
    return output_md


def maybe_generate_pdf(md_path: Path) -> Path | None:
    pandoc = shutil.which("pandoc")
    if not pandoc:
        print("[info] pandoc not found; skipping PDF generation")
        return None
    pdf_path = md_path.with_suffix(".pdf")
    cmd = [
        pandoc,
        str(md_path),
        "-o",
        str(pdf_path),
        "--from=gfm",
        "-V",
        "geometry:margin=1in",
    ]
    try:
        subprocess.run(cmd, check=True)
        return pdf_path
    except subprocess.CalledProcessError as exc:
        print(f"[warn] pandoc failed: {exc}")
        return None


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    md = build_progression(root)
    print(f"[ok] Wrote {md}")
    pdf = maybe_generate_pdf(md)
    if pdf:
        print(f"[ok] Wrote {pdf}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

