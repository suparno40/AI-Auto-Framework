from prompt_engine.builder import build_prompt
from ai_runner.runner import run

prompt = build_prompt(
    role="job_hunter",
    task="search_job",
    output="json"
)

response = run(prompt)

print(response)
