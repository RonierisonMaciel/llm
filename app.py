import streamlit as st
from utils import generate_response

st.title("🏦 BDI (Banco de Dados Intelligence)")

with st.sidebar:
    st.header("Histórico de Consultas")
    if st.button("Mostrar Histórico"):
        import sqlite3
        from config import CACHE_DB_PATH

        conn = sqlite3.connect(CACHE_DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT pergunta, resposta FROM historico ORDER BY id DESC")
        historico = cursor.fetchall()
        conn.close()

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
