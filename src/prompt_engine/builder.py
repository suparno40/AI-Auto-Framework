import logging
from typing import Optional

logger = logging.getLogger(__name__)

PROMPT_TEMPLATES = {
    "job_hunter_search_job_json": """
You are an expert job search assistant. Analyze the following job vacancies and provide:
1. Top 3 best matches for the user
2. Key skills required for each position
3. Salary insights
4. Career growth opportunities

Provide response in JSON format with the following structure:
{
    "best_matches": [
        {"position": "...", "company": "...", "match_score": 0.0, "reason": "..."}
    ],
    "key_skills": [...],
    "salary_insights": "...",
    "career_advice": "..."
}
""",
    
    "job_hunter_search_job_text": """
You are an expert job search assistant. Analyze the following job vacancies and provide:
1. Top 3 best matches for the user
2. Key skills required for each position
3. Salary insights
4. Career growth opportunities

Provide a detailed, readable analysis in plain text format.
""",
}

def build_prompt(role: str = "job_hunter", task: str = "search_job", output: str = "text") -> str:
    """
    Build prompt berdasarkan role, task, dan output format
    
    Args:
        role (str): Role/persona (e.g., 'job_hunter', 'developer')
        task (str): Task yang akan dilakukan (e.g., 'search_job')
        output (str): Format output ('json' atau 'text')
        
    Returns:
        str: Prompt yang sudah di-build
    """
    try:
        # Build key untuk lookup template
        template_key = f"{role}_{task}_{output}"
        
        # Ambil template atau gunakan default
        if template_key in PROMPT_TEMPLATES:
            prompt = PROMPT_TEMPLATES[template_key]
        else:
            # Fallback ke generic prompt
            prompt = f"""
You are a helpful assistant with expertise in {role}.
Task: {task.replace('_', ' ')}
Output format: {output}

Provide a comprehensive and helpful response.
"""
            logger.warning(f"Template tidak ditemukan untuk {template_key}, menggunakan generic prompt")
        
        logger.info(f"Prompt berhasil di-build untuk {role}/{task} -> {output}")
        return prompt
        
    except Exception as e:
        logger.error(f"Error saat build prompt: {str(e)}")
        return "Please provide a helpful response."
