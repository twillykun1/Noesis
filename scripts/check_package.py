#!/usr/bin/env python3
"""Validate the isolated Noesis distribution using only the standard library."""
from pathlib import Path
import re
import stat
import sys
from urllib.parse import unquote, urlsplit

FILES = {'SKILL.md', 'examples/scenarios.md', 'references/review.md', 'references/complex-projects.md', 'references/preferences.md', 'templates/decision-record.md'}
DIRS = {'examples', 'references', 'templates'}

def check(package):
    package = Path(package)
    errors = []
    if package.is_symlink() or not package.is_dir():
        return ['package must be a regular directory']
    found = set()
    texts = {}
    for item in package.rglob('*'):
        relative = item.relative_to(package).as_posix()
        mode = item.lstat().st_mode
        if stat.S_ISDIR(mode):
            if relative not in DIRS:
                errors.append(f'unexpected directory: {relative}')
            continue
        if not stat.S_ISREG(mode):
            errors.append(f'nonregular asset: {relative}')
            continue
        found.add(relative)
        if relative not in FILES:
            errors.append(f'unexpected asset: {relative}')
        try:
            texts[relative] = item.read_text(encoding='utf-8')
        except UnicodeError:
            errors.append(f'not UTF-8: {relative}')
    if found != FILES:
        errors.append(f'file set differs: {sorted(found ^ FILES)}')
    core = texts.get('SKILL.md', '')
    # Deliberately validate the small supported frontmatter schema, not arbitrary YAML.
    header = re.match(r'\A---\nname: noesis\ndescription: (Use when[^\n]{1,1016})\nmetadata:\n  version: "0\.4\.0"\n---\n', core)
    if header and ': ' in header.group(1):
        errors.append('unsupported description scalar syntax')
    if not header:
        errors.append('invalid Noesis frontmatter')
    for relative, content in texts.items():
        links = re.findall(r'\[[^\]]*\]\(([^)]+)\)', content)
        links += re.findall(r'^\s*\[[^\]]+\]:\s*(\S+)', content, re.MULTILINE)
        for link in links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                errors.append(f'external dependency in {relative}: {link}')
                continue
            target = (package / relative).parent / unquote(parsed.path)
            try:
                target.resolve().relative_to(package.resolve())
            except ValueError:
                errors.append(f'escaping link in {relative}: {link}')
                continue
            if not target.is_file() or target.is_symlink():
                errors.append(f'missing/nonregular link in {relative}: {link}')
    return errors

if __name__ == '__main__':
    issues = check(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / 'skills/noesis')
    print('\n'.join(issues) if issues else 'Noesis package valid')
    raise SystemExit(bool(issues))
