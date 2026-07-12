from ai_runner.response import AIResponse


def ask(provider, prompt):

    return AIResponse(
        provider=provider,
        prompt=prompt,
        output=f"[SIMULASI {provider.upper()}]\n\n{prompt[:300]}..."
    )
