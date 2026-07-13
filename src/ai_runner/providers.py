from ai_runner.response import AIResponse
from ai_runner.config import DEFAULT_PROVIDER, AVAILABLE_PROVIDERS
import logging

logger = logging.getLogger(__name__)


def ask(provider, prompt):
    """
    Mengirim prompt ke provider AI yang dipilih.
    
    Args:
        provider (str): Nama provider AI (chatgpt, gemini, claude, grok)
        prompt (str): Prompt yang akan dikirim
        
    Returns:
        AIResponse: Objek respons dengan provider, prompt, dan output
    """
    
    if provider not in AVAILABLE_PROVIDERS:
        logger.warning(f"Provider '{provider}' tidak dikenal. Menggunakan default: {DEFAULT_PROVIDER}")
        provider = DEFAULT_PROVIDER
    
    try:
        # Route ke provider yang sesuai
        if provider == "chatgpt":
            from ai_runner.providers.openai_provider import ask as openai_ask
            output = openai_ask(prompt)
        elif provider == "gemini":
            # TODO: Implementasi Gemini provider
            logger.warning("Gemini provider belum diimplementasikan")
            output = f"[PENDING] Gemini provider akan segera hadir"
        elif provider == "claude":
            # TODO: Implementasi Claude provider
            logger.warning("Claude provider belum diimplementasikan")
            output = f"[PENDING] Claude provider akan segera hadir"
        elif provider == "grok":
            # TODO: Implementasi Grok provider
            logger.warning("Grok provider belum diimplementasikan")
            output = f"[PENDING] Grok provider akan segera hadir"
        else:
            output = "Provider tidak dikenali"
            
    except Exception as e:
        logger.error(f"Error saat memanggil {provider}: {str(e)}")
        output = f"Error: {str(e)}"
    
    return AIResponse(
        provider=provider,
        prompt=prompt,
        output=output
    )
