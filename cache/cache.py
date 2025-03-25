import os
import sqlite3
import streamlit as st
from gpt4all import GPT4All
from config.config import MODEL_PATH, CACHE_DB_PATH
from config.config import DB_PATH, CACHE_DB_PATH

# 🧠 Cache da Estrutura do Banco
@st.cache_resource
def get_database_schema():
    """Obtém e armazena a estrutura do banco de dados."""
    try:
        conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)  # Apenas leitura
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if not tables:
            st.warning("⚠ Nenhuma tabela encontrada no banco de dados.")
            return {}

        schema = {}
        for table in tables:
            table_name = table[0]
            cursor.execute(f'PRAGMA table_info("{table_name}");')
            columns = [col[1] for col in cursor.fetchall()]
            schema[table_name] = columns

        conn.close()
        return schema
    except Exception as e:
        st.error(f"❌ Erro ao buscar estrutura do banco: {str(e)}")
        return {}
    

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


# 🧠 Cache do Modelo
@st.cache_resource
def load_model():
    """Carrega o modelo GPT4All apenas uma vez."""
    if not os.path.exists(MODEL_PATH):
        st.error(f"❌ Modelo não encontrado: {MODEL_PATH}")
        return None
    try:
        return GPT4All(MODEL_PATH)
    except Exception as e:
        st.error(f"❌ Erro ao carregar o modelo GPT4All: {str(e)}")
        return None

model = load_model()
if model:
    st.success("✅ Modelo carregado com sucesso!")
