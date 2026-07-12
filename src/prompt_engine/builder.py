from prompt_engine.registry import get_by_name


def build_prompt(*names):
    result = []

    for name in names:
        prompt = get_by_name(name)

        if prompt:
            result.append(prompt.content)

    return "\n\n".join(result)


def main():
    final_prompt = build_prompt(
        "base",
        "indonesia",
        "job_hunter",
        "search_job"
    )

    print(final_prompt[:1000])  # tampilkan 1000 karakter pertama


if __name__ == "__main__":
    main()
