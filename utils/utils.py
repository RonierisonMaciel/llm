import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env automaticamente
load_dotenv()

# Uso das variáveis carregadas
DB_PATH = os.getenv("DB_PATH", "banco_padrao.db")
MODEL_PATH = os.getenv("MODEL_PATH", "modelo.pkl")
CACHE_DB_PATH = os.getenv("CACHE_DB_PATH", "cache_respostas.db")
