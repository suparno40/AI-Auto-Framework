from ai_runner.config import DEFAULT_PROVIDER
from ai_runner.providers import ask


def run(prompt, provider=DEFAULT_PROVIDER):

    return ask(provider, prompt)


def main():

    prompt = "Halo AI"

    result = run(prompt)

    print(result)


if __name__ == "__main__":
    main()
