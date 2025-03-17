from config import CACHE_DB_PATH
import sqlite3

# 🧠 Criar ou Carregar Cache de Perguntas e Respostas
def init_cache_db():
    """Cria o banco de cache para aprendizado se não existir."""
    conn = sqlite3.connect(CACHE_DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pergunta TEXT UNIQUE,
            resposta TEXT
        );
    """)
    conn.commit()
    conn.close()

init_cache_db()

def salvar_resposta(pergunta, resposta):
    """Armazena a pergunta e resposta no cache para aprendizado futuro."""
    conn = sqlite3.connect(CACHE_DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO historico (pergunta, resposta) VALUES (?, ?)", (pergunta, resposta))
    conn.commit()
    conn.close()

def buscar_resposta_cache(pergunta):
    """Verifica se já existe uma resposta no cache."""
    conn = sqlite3.connect(CACHE_DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT resposta FROM historico WHERE pergunta = ?", (pergunta,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado else None
