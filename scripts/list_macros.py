#!/usr/bin/env python3
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]  # repo/
DOCS = ROOT / "docs"
PAT = re.compile(r"\\(re)?newcommand\*?\s*{\\([A-Za-z@]+)}")

def scan_file(path):
    txt = path.read_text(errors="ignore")
    return [(path, m.group(2)) for m in PAT.finditer(txt)]

def main():
    hits = []
    for p in DOCS.rglob("*.tex"):
        # Ignora macros globales
        if p.name in ("pdo-macros.tex", "pdo-conventions.tex"):
            continue
        hits.extend(scan_file(p))
    # Reporte
    out = []
    for path, macro in hits:
        out.append(f"{path.relative_to(ROOT)} :: \\{macro}")
    rep = "\n".join(sorted(out))
    (DOCS / "macro_scan.md").write_text(rep or "(sin macros locales)")
    print("Hecho. Ver docs/macro_scan.md")

if __name__ == "__main__":
    main()
