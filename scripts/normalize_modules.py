#!/usr/bin/env python3
"""
Normalize foundations/modules:
- Rename files from week-XX.md → 01-workshop-safety-and-labeling.md (concept-based)
- Strip "Week NN —" from top heading inside each module file
- Regenerate modules/README.md with links in order
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


MODULES_DIR = Path(__file__).resolve().parents[1] / "curriculum" / "mechanics" / "foundations" / "modules"
INDEX_PATH = MODULES_DIR / "README.md"


def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def write_text(p: Path, s: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")


def slugify(title: str) -> str:
    t = title.strip().lower()
    t = re.sub(r"[’'“”]", "", t)
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t


def extract_concept_and_number(md: str, fallback_num: int | None) -> tuple[str, int | None]:
    # Look for heading like: ### Week 01 — Concept Title
    for line in md.splitlines():
        if line.startswith("### "):
            m = re.match(r"^###\s+Week\s+(\d+)\s+[—-]\s*(.+)$", line.strip())
            if m:
                return m.group(2).strip(), int(m.group(1))
            # If already normalized, just return heading text without hashes
            return line.lstrip('#').strip(), fallback_num
    return ("module", fallback_num)


def update_heading_remove_week(md: str) -> str:
    out = []
    replaced = False
    for line in md.splitlines():
        if not replaced and line.startswith("### "):
            m = re.match(r"^(#{3,6})\s+Week\s+\d+\s+[—-]\s*(.+)$", line.strip())
            if m:
                out.append(f"{m.group(1)} {m.group(2)}")
                replaced = True
                continue
        out.append(line)
    return "\n".join(out) + ("\n" if not md.endswith("\n") else "")


def git_mv(old: Path, new: Path) -> None:
    subprocess.run(["git", "mv", str(old), str(new)], check=True)


def main() -> int:
    if not MODULES_DIR.exists():
        print("[error] modules dir not found")
        return 1

    rename_pairs: list[tuple[Path, Path]] = []
    index_entries: list[tuple[int, str, Path]] = []

    for md_path in sorted(MODULES_DIR.glob("*.md")):
        if md_path.name.lower() == "readme.md":
            continue
        content = read_text(md_path)
        # determine number from filename if present
        mnum = re.match(r"^(?:week|module)?-?(\d{1,2})", md_path.stem)
        num_from_name = int(mnum.group(1)) if mnum else None
        concept, number = extract_concept_and_number(content, num_from_name)
        # update heading
        updated = update_heading_remove_week(content)
        write_text(md_path, updated)
        # build new name
        num_prefix = f"{number:02d}-" if number is not None else ""
        new_name = num_prefix + slugify(concept) + ".md"
        new_path = md_path.with_name(new_name)
        if new_path.name != md_path.name:
            rename_pairs.append((md_path, new_path))
        index_entries.append((number or 999, concept, new_path))

    # Perform renames via git mv for history
    for old, new in rename_pairs:
        git_mv(old, new)

    # Recompute final list after renames
    index_entries = [(n, t, MODULES_DIR / (f"{n:02d}-" + slugify(t) + ".md")) for n, t, _ in index_entries]
    index_entries.sort(key=lambda x: x[0])

    # Rewrite README index with links
    lines = [
        "### Foundations modules (index)",
        "",
        "Use these modules with the templates in `../../templates/` and the main `../syllabus.md`.",
        "",
    ]
    for n, title, path in index_entries:
        rel = path.name
        lines.append(f"- [{title}]({rel})")
    write_text(INDEX_PATH, "\n".join(lines) + "\n")

    print("[ok] normalized modules and updated index")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

