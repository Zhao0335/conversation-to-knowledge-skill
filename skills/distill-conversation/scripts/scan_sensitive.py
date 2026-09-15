#!/usr/bin/env python3

import argparse
from pathlib import Path

MARKERS = ("password=", "token=", "secret=", "api_key=")


def scan_text(text: str):
    lowered = text.lower()
    return [marker for marker in MARKERS if marker in lowered]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    files = [args.path] if args.path.is_file() else list(args.path.rglob("*.md"))
    findings = []
    for file in files:
        for marker in scan_text(file.read_text(encoding="utf-8")):
            findings.append((file, marker))
    for file, marker in findings:
        print(f"review: {file}: {marker}")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
