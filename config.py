import os

# 📌 Caminhos do Banco de Dados e do Modelo (definidos pelo usuário)
DB_PATH = os.getenv("DB_PATH", "banco_padrao.db")  # Usa um banco padrão se não for definido
CACHE_DB_PATH = os.getenv("CACHE_DB_PATH", "cache_respostas.db")  # Cache para aprendizado
