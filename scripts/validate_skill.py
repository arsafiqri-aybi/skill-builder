#!/usr/bin/env python3
"""Unified Skill Builder validation entry point."""

import argparse
import json
import sys
from pathlib import Path

from audit_skill import audit


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_directory")
    parser.add_argument("--portable", action="store_true")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    root = Path(args.skill_directory)
    try:
        report = audit(root, portable=args.portable)
    except (OSError, RuntimeError) as exc:
        print(f"Validasi tidak dapat berjalan: {exc}", file=sys.stderr)
        return 2

    if args.as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("Skill valid." if report["ok"] else "Skill belum valid.")
        for item in report["issues"]:
            print(f'{item["level"]}: {item["file"]}: {item["message"]}')
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
