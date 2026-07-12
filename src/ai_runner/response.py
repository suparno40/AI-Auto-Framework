class AIResponse:

    def __init__(self, provider, prompt, output):
        self.provider = provider
        self.prompt = prompt
        self.output = output

    def __str__(self):
        return self.output
