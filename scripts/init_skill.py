#!/usr/bin/env python3
"""Create a minimal Skill scaffold without overwriting existing work."""

import argparse
import re
import sys
from pathlib import Path

from build_metadata import write_metadata


ALLOWED_RESOURCES = {"references", "scripts", "assets"}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def normalize_name(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value


def parse_resources(value: str):
    if not value:
        return []
    result = []
    for raw in value.split(","):
        item = raw.strip()
        if not item:
            continue
        if item not in ALLOWED_RESOURCES:
            raise ValueError(f"Resource tidak dikenal: {item}")
        if item not in result:
            result.append(item)
    return result


def init_skill(raw_name: str, parent: Path, description: str, resources):
    name = normalize_name(raw_name)
    if not NAME_RE.fullmatch(name) or len(name) > 64:
        raise ValueError("Nama Skill tidak sah setelah normalisasi.")
    description = description.strip()
    if not description or len(description) > 1024 or "<" in description or ">" in description:
        raise ValueError("Description wajib, maksimal 1024 karakter, tanpa angle bracket.")

    target = parent.resolve() / name
    if target.exists():
        raise FileExistsError(f"Target sudah ada: {target}")

    target.mkdir(parents=True)
    title = " ".join(part.capitalize() for part in name.split("-"))
    body = (
        "---\n"
        f"name: {name}\n"
        f"description: {description}\n"
        "---\n\n"
        f"# {title}\n\n"
        "## Tujuan\n\n"
        "Jelaskan hasil konkret yang harus dihasilkan Skill ini.\n\n"
        "## Workflow\n\n"
        "1. Tetapkan input, batas, dan sumber kebenaran.\n"
        "2. Kerjakan prosedur inti dengan alat yang benar-benar tersedia.\n"
        "3. Periksa hasil terhadap kriteria penerimaan.\n\n"
        "## Batas\n\n"
        "Jelaskan permintaan yang tidak seharusnya ditangani oleh Skill ini.\n"
    )
    (target / "SKILL.md").write_text(body, encoding="utf-8")

    for resource in resources:
        (target / resource).mkdir()

    write_metadata(target)
    return target


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("--path", required=True)
    parser.add_argument("--description", required=True)
    parser.add_argument("--resources", default="")
    args = parser.parse_args()
    try:
        resources = parse_resources(args.resources)
        target = init_skill(args.name, Path(args.path), args.description, resources)
    except (OSError, ValueError) as exc:
        print(f"Scaffold gagal dibuat: {exc}", file=sys.stderr)
        return 1
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
