#!/usr/bin/env python3

from pathlib import Path


def print_header():
    print("=" * 40)
    print(" AI AUTO FRAMEWORK")
    print(" Prompt Loader v1.1")
    print("=" * 40)
    print()


def scan_prompt_files():
    # Lokasi folder prompts
    project_root = Path(__file__).resolve().parents[2]
    prompts_dir = project_root / "prompts"

    print("Scanning prompts...\n")

    if not prompts_dir.exists():
        print("Folder 'prompts' tidak ditemukan!")
        return []

    markdown_files = sorted(prompts_dir.rglob("*.md"))

    if not markdown_files:
        print("Tidak ada file markdown ditemukan.")
        return []

    for file in markdown_files:
        relative = file.relative_to(project_root)
        print(f"✓ {relative}")

    return markdown_files


def main():
    print_header()

    files = scan_prompt_files()

    print("\n" + "-" * 40)
    print(f"Total Markdown : {len(files)}")
    print("-" * 40)


if __name__ == "__main__":
    main()
