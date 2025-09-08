#!/usr/bin/env python3
import json
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent

DEFAULT_ORDER = [
    "README.md",
    "Curriculum_Overview.md",
    "Scope_and_Sequence.md",
    "Weekly_Sessions.md",
    "Parent_Scripts_Age3.md",
    "Parent_Scripts_Age5.md",
    "Progress_Tracker.md",
]

def load_manifest():
    manifest_path = ROOT / "MANIFEST.json"
    if manifest_path.exists():
        with open(manifest_path, "r", encoding="utf-8") as f:
            try:
                manifest = json.load(f)
                order = manifest.get("order", [])
                return [str(Path(p)) for p in order if (ROOT / p).exists()]
            except json.JSONDecodeError:
                pass
    return DEFAULT_ORDER

def read_file(path: Path) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()

def build_markdown(output_name: str = "Curriculum_Compiled.md") -> Path:
    order = load_manifest()
    parts = []
    for rel in order:
        p = ROOT / rel
        if not p.exists():
            continue
        parts.append(f"\n\n---\n\n")
        parts.append(f"<!-- {rel} -->\n\n")
        parts.append(read_file(p))
    compiled = "".join(parts).lstrip()
    out_path = ROOT / output_name
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(compiled)
    return out_path

def build_pdf(md_path: Path, output_pdf: str = "Curriculum_Compiled.pdf") -> Path:
    # Try pandoc if available
    pdf_path = md_path.with_suffix(".pdf") if output_pdf == "" else ROOT / output_pdf
    try:
        subprocess.run(
            ["pandoc", str(md_path), "-o", str(pdf_path)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return pdf_path
    except Exception:
        print("pandoc not available; skipping PDF build.")
        return pdf_path

if __name__ == "__main__":
    md_out = build_markdown()
    print(f"Wrote {md_out}")
    # attempt optional PDF
    build_pdf(md_out)
    
