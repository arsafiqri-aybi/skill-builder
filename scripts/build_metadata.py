#!/usr/bin/env python3
"""Generate agents/openai.yaml from a Skill's canonical identity."""

import argparse
import re
import sys
from pathlib import Path

import yaml


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def read_identity(skill_dir: Path):
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        raise ValueError("SKILL.md tidak ditemukan.")
    text = skill_file.read_text(encoding="utf-8")
    match = re.match(r"\A---[ \t]*\n(.*?)\n---[ \t]*(?:\n|\Z)", text, re.S)
    if not match:
        raise ValueError("Frontmatter SKILL.md tidak sah.")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError("Frontmatter harus berupa mapping.")
    name = data.get("name")
    if not isinstance(name, str) or not NAME_RE.fullmatch(name) or len(name) > 64:
        raise ValueError("name tidak sah.")
    return name


def default_display_name(name: str) -> str:
    return " ".join(part.capitalize() for part in name.split("-"))


def default_short_description(display_name: str) -> str:
    text = f"Build and maintain reliable {display_name} workflows"
    if len(text) < 25:
        text += " for AI tasks"
    return text[:64].rstrip()


def yaml_text(value: str) -> str:
    return yaml.safe_dump(value, allow_unicode=True, default_flow_style=True).strip()


def write_metadata(skill_dir: Path, display_name=None, short_description=None,
                   default_prompt=None):
    name = read_identity(skill_dir)
    display_name = display_name or default_display_name(name)
    short_description = short_description or default_short_description(display_name)
    default_prompt = default_prompt or f"Use ${name} to handle this task."

    if not 1 <= len(display_name) <= 80:
        raise ValueError("display_name harus 1–80 karakter.")
    if not 25 <= len(short_description) <= 64:
        raise ValueError("short_description harus 25–64 karakter.")
    if f"${name}" not in default_prompt:
        raise ValueError("default_prompt harus memanggil runtime identifier Skill.")

    agents = skill_dir / "agents"
    agents.mkdir(parents=True, exist_ok=True)
    target = agents / "openai.yaml"
    target.write_text(
        "interface:\n"
        f"  display_name: {yaml_text(display_name)}\n"
        f"  short_description: {yaml_text(short_description)}\n"
        f"  default_prompt: {yaml_text(default_prompt)}\n",
        encoding="utf-8",
    )
    return target


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_directory")
    parser.add_argument("--display-name")
    parser.add_argument("--short-description")
    parser.add_argument("--default-prompt")
    args = parser.parse_args()
    try:
        target = write_metadata(
            Path(args.skill_directory).resolve(),
            args.display_name,
            args.short_description,
            args.default_prompt,
        )
    except (OSError, UnicodeError, ValueError, yaml.YAMLError) as exc:
        print(f"Metadata gagal dibuat: {exc}", file=sys.stderr)
        return 1
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
