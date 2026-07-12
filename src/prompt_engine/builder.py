from prompt_engine.registry import get_by_name
from prompt_engine.config import (
    DEFAULT_SYSTEM,
    DEFAULT_LANGUAGE,
    DEFAULT_VALIDATORS,
)


def build_prompt(
    role,
    task,
    language=DEFAULT_LANGUAGE,
    output=None,
    validators=None,
):
    if validators is None:
        validators = DEFAULT_VALIDATORS

    names = [
        DEFAULT_SYSTEM,
        language,
        role,
        task,
    ]

    if output:
        names.append(output)

    names.extend(validators)

    result = []

    for name in names:
        prompt = get_by_name(name)

        if prompt:
            result.append(prompt.content)

    return "\n\n".join(result)


def main():
    prompt = build_prompt(
        role="job_hunter",
        task="search_job",
        output="json",
    )

    print(prompt[:1500])


if __name__ == "__main__":
    main()
