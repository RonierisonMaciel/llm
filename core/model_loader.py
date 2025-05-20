from functools import lru_cache
from langchain_ollama import OllamaLLM
import logging
import os

logger = logging.getLogger(__name__)

@lru_cache(maxsize=3)
def load_ollama_model(model_name: str = None) -> OllamaLLM:
    model = model_name or os.getenv("MODEL_NAME")
    
    if not model:
        raise ValueError("Variável MODEL_NAME não definida no .env!")
    
    try:
        return OllamaLLM(model=model)
    except Exception as e:
        logger.error(f"Erro ao carregar o modelo {model}: {e}")
        raise RuntimeError(f"Modelo não disponível: {model}. Execute `ollama pull {model}`.")