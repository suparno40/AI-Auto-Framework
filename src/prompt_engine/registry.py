from loader import load_prompts


def get_by_category(category: str):
    prompts = load_prompts()
    return [p for p in prompts if p.category == category]


def get_by_name(name: str):
    prompts = load_prompts()

    for p in prompts:
        if p.name == name:
            return p

    return None


def main():
    print("=== Prompt Registry ===\n")

    systems = get_by_category("system")

    print("SYSTEM PROMPTS")
    for p in systems:
        print("-", p.name)

    print()

    prompt = get_by_name("search_job")

    if prompt:
        print("FOUND :", prompt.name)
        print(prompt.path)


if __name__ == "__main__":
    main()
