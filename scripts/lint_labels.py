#!/usr/bin/env python3
"""
Busca ecuaciones sin \\label dentro de entornos equation/align.
Uso: python scripts/lint_labels.py docs > lint_labels.log
"""
import sys, pathlib, re

BEGIN_EQ = re.compile(r'\\begin\\{(equation\\*?|align\\*?)\\}')
END_EQ   = re.compile(r'\\end\\{(equation\\*?|align\\*?)\\}')
LABEL    = re.compile(r'\\label\\{[^}]+\\}')


def check_file(path: pathlib.Path):
    with path.open('r', errors='ignore') as f:
        buf = f.read().splitlines()
    in_eq = False
    start = 0
    has_label = False
    for i, line in enumerate(buf, 1):
        if not in_eq and BEGIN_EQ.search(line):
            in_eq = True
            start = i
            has_label = False
        elif in_eq:
            if LABEL.search(line):
                has_label = True
            if END_EQ.search(line):
                if not has_label and not line.strip().endswith('*}'):  # starless env only if not suppressed
                    yield start, i
                in_eq = False
    # handle file end inside eq (rare)
    if in_eq and not has_label:
        yield start, len(buf)


def main():
    root = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path('docs')
    issues = 0
    for tex in root.rglob('*.tex'):
        for a, b in check_file(tex):
            issues += 1
            print(f'{tex}:{a}-{b}: equation/align without \\label')
    if issues == 0:
        print('OK: all equation/align envs have labels.')

if __name__ == '__main__':
    main()
