from openai import OpenAI
import os
import logging

logger = logging.getLogger(__name__)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def ask(prompt):
    """
    Mengirim prompt ke OpenAI API dan mengembalikan respons.
    
    Args:
        prompt (str): Prompt yang akan dikirim ke AI
        
    Returns:
        str: Respons dari OpenAI
    """
    try:
        if not os.getenv("OPENAI_API_KEY"):
            return "Error: OPENAI_API_KEY tidak ditemukan di environment"
            
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Fixed: gpt-4.1-mini tidak valid, gunakan gpt-3.5-turbo
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=2000
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"OpenAI API Error: {str(e)}")
        return f"Error: {str(e)}"
