#!/usr/bin/env python3
"""
Detecta usos de GeV y sugiere conversión a eV (Issue #3 ULDM→eV).
Uso: python scripts/lint_units.py docs > lint_units.log
"""
import sys, re, pathlib

GEV_PAT = re.compile(r'(GeV|\\mathrm\{GeV\}|\\si\{[^}]*giga[^}]*electronvolt[^}]*\})')


def scan(path: pathlib.Path):
    with path.open('r', errors='ignore') as f:
        for i, line in enumerate(f, 1):
            if GEV_PAT.search(line):
                yield i, line.rstrip('\n')


def main():
    root = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path('docs')
    hits = 0
    for tex in root.rglob('*.tex'):
        for lineno, snippet in scan(tex):
            hits += 1
            print(f'{tex}:{lineno}: POSSIBLE GeV -> use eV (x1e9). Line: {snippet}')
    if hits == 0:
        print('OK: no GeV patterns detected.')


if __name__ == '__main__':
    main()
