#!/usr/bin/env python3

import argparse
from pathlib import Path


def validate(path: Path):
    files = [path] if path.is_file() else sorted(path.rglob("*.md"))
    errors = []
    warnings = []
    if not files:
        errors.append("no Markdown files found")
    for file in files:
        if not file.read_text(encoding="utf-8").strip():
            errors.append(f"empty Markdown file: {file}")
    if path.is_dir() and len(files) > 1 and not (path / "index.md").exists():
        warnings.append("multi-file bundle has no index.md")
    return errors, warnings


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    errors, warnings = validate(args.path)
    for item in warnings:
        print(f"warning: {item}")
    for item in errors:
        print(f"error: {item}")
    return 2 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
