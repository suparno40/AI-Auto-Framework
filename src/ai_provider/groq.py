import os
import logging
from groq import Groq

logger = logging.getLogger(__name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_ai(prompt: str) -> str:
    """
    Mengirim prompt ke Groq AI dan mengembalikan respons.
    
    Args:
        prompt (str): Prompt yang akan dikirim ke AI
        
    Returns:
        str: Respons dari Groq AI
    """
    try:
        if not os.getenv("GROQ_API_KEY"):
            logger.warning("GROQ_API_KEY tidak ditemukan di environment")
            return "Error: GROQ_API_KEY tidak ditemukan. Silakan setup di .env"
        
        message = client.messages.create(
            model="mixtral-8x7b-32768",  # Model Groq yang paling capable dan gratis
            max_tokens=2048,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        
        logger.info("Respons dari Groq AI berhasil diterima")
        return message.content[0].text
        
    except Exception as e:
        logger.error(f"Groq API Error: {str(e)}")
        return f"Error: Gagal mendapatkan respons dari Groq AI - {str(e)}"
