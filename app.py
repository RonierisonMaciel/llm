import streamlit as st
from utils import generate_response

st.title("🏦 BDI (Banco de Dados Intelligence)")

# ---------- Sidebar para exibir o histórico de consultas ----------
with st.sidebar:
    st.header("Histórico de Consultas")
    if st.button("Mostrar Histórico"):
        import sqlite3
        from config import CACHE_DB_PATH

        # Conecta ao banco de cache e busca o histórico de consultas, ordenando o mais recente primeiro
        conn = sqlite3.connect(CACHE_DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT pergunta, resposta FROM historico ORDER BY id DESC")
        historico = cursor.fetchall()
        conn.close()

        # Exibe os registros do histórico se houver
        if historico:
            for pergunta, resposta in historico:
                st.write("**Pergunta:**", pergunta)
                st.write("**Resposta:**", resposta)
                st.markdown("---")
        else:
            st.write("Nenhum histórico encontrado.")

# ---------- Interface Principal ----------
with st.form("query_form"):
    user_input = st.text_area("Digite sua pergunta:", "Qual foi o último valor do IPCA em Recife?")
    submitted = st.form_submit_button("Consultar")

    if submitted:
        response = generate_response(user_input)
        st.markdown(response)
