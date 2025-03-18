import os
from dotenv import load_dotenv

# 📌 Carregar configurações do `.env`
load_dotenv()

# 📌 Caminhos do Banco de Dados e do Modelo (definidos pelo usuário)
DB_PATH = os.getenv("DB_PATH", "banco_padrao.db")  # Usa um banco padrão se não for definido
CACHE_DB_PATH = os.getenv("CACHE_DB_PATH", "cache_respostas.db")  # Cache para aprendizado

modelo_path = os.getenv(
    "MODEL_PATH", 
    "~/Library/Application Support/nomic.ai/GPT4All/Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf"
)
