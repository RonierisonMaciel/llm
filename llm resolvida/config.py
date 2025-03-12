import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configurações do Banco de Dados
DB_PATH = os.getenv("DB_PATH", "banco_padrao.db")
CACHE_DB_PATH = os.getenv("CACHE_DB_PATH", "cache_respostas.db")

# Configuração do caminho do Modelo
MODEL_PATH = os.getenv(
    "MODEL_PATH", 
    "~/Library/Application Support/nomic.ai/GPT4All/Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf"
)
