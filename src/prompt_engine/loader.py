#!/usr/bin/env python3

from pathlib import Path
from dataclasses import dataclass


@dataclass
class PromptFile:
    path: str
    category: str
    name: str
    content: str


def print_header():
    print("=" * 40)
    print(" AI AUTO FRAMEWORK")
    print(" Prompt Loader v1.2")
    print("=" * 40)
    print()


def load_prompts():
    project_root = Path(__file__).resolve().parents[2]
    prompts_dir = project_root / "prompts"

    prompt_files = []

    for file in sorted(prompts_dir.rglob("*.md")):
        content = file.read_text(encoding="utf-8")

        prompt = PromptFile(
            path=str(file.relative_to(project_root)),
            category=file.parent.name,
            name=file.stem,
            content=content
        )

        prompt_files.append(prompt)

    return prompt_files


def main():
    print_header()

    prompts = load_prompts()

    for p in prompts:
        print(f"✓ {p.path}")
        print(f"  Category : {p.category}")
        print(f"  Name     : {p.name}")
        print(f"  Length   : {len(p.content)} karakter\n")

    print("-" * 40)
    print(f"Total Markdown : {len(prompts)}")
    print("-" * 40)


if __name__ == "__main__":
    main()
