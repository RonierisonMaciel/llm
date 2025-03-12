import streamlit as st
import sqlite3
from config import DB_PATH

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

def query_database(query):
    """Executa uma consulta no banco de dados SQLite."""
    try:
        conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)  # Apenas leitura
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result
    except sqlite3.Error as e:
        return f"❌ Erro ao executar a consulta: {str(e)}"
