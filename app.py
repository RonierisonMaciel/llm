import os
import streamlit as st
import sqlite3
from gpt4all import GPT4All
from dotenv import load_dotenv

st.title("🏦 BDI (Banco de Dados Intelligence)")

# 📌 Carregar configurações do `.env`
load_dotenv()

# 📌 Caminhos do Banco de Dados e do Modelo (definidos pelo usuário)
DB_PATH = os.getenv("DB_PATH", "banco_padrao.db")  # Usa um banco padrão se não for definido
CACHE_DB_PATH = os.getenv("CACHE_DB_PATH", "cache_respostas.db")  # Cache para aprendizado

modelo_path = os.getenv(
    "MODEL_PATH", 
    "~/Library/Application Support/nomic.ai/GPT4All/Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf"
)

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

def generate_response(user_question):
    """Busca no cache ou gera uma nova resposta se necessário."""

    if model is None:
        return "❌ O modelo não foi carregado corretamente."

    if not user_question.strip():
        return "❌ Por favor, insira uma pergunta válida."

    # 🔥 Primeiro, verifica se a resposta já está no cache
    resposta_cache = buscar_resposta_cache(user_question)
    if resposta_cache:
        return f"📌 **Resposta recuperada do histórico:**\n\n{resposta_cache}"

    # 🔍 Obtém a estrutura do banco
    schema = get_database_schema()
    if not schema:
        return "❌ Erro ao buscar a estrutura do banco de dados."

    # Identificar a tabela mais relevante
    table_to_query = None
    for table in schema.keys():
        if table.lower() in user_question.lower():
            table_to_query = table
            break

    # Se nenhuma tabela for encontrada, listar as tabelas disponíveis
    if not table_to_query:
        return f"📊 O banco contém as seguintes tabelas:\n" + "\n".join([f"- {table}" for table in schema.keys()])

    # 🔍 Consulta otimizada (busca apenas colunas mais relevantes)
    columns = ", ".join(schema[table_to_query][:5])  # Limita a 5 colunas para otimizar
    query = f'SELECT {columns} FROM "{table_to_query}" ORDER BY ROWID DESC LIMIT 5;'
    result = query_database(query)

    if isinstance(result, str):
        return result  # Retorna erro de SQL, se houver

    # 🔥 Agora pedimos para a LLM interpretar os dados
    dados_texto = "\n".join([", ".join(map(str, row)) for row in result])
    prompt = f"""
    Você é um assistente que responde perguntas sobre um banco de dados.
    Aqui estão os últimos registros extraídos:

    {dados_texto}

    Com base nesses dados, responda à seguinte pergunta de forma clara e objetiva:
    "{user_question}"
    """

    try:
        resposta = model.generate(prompt).strip()

        # 🔥 Salvar resposta no cache para aprendizado futuro
        salvar_resposta(user_question, resposta)

        return resposta
    except Exception as e:
        return f"❌ Erro ao processar a solicitação: {str(e)}"

# 🎛️ Interface no Streamlit
with st.form("query_form"):
    user_input = st.text_area("Digite sua pergunta:", "Qual foi o último valor do IPCA em Recife?")
    submitted = st.form_submit_button("Consultar")

    if submitted:
        response = generate_response(user_input)
        st.markdown(response)
