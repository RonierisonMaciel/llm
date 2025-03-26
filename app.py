import streamlit as st
from model.model import generate_response

st.title("🏦 BDI (Banco de Dados Inteligente)")

# 🎛️ Interface no Streamlit
with st.form("query_form"):
    user_input = st.text_area("Digite sua pergunta:", "Quais são as tabelas contidas no Bando de Dados?")
    submitted = st.form_submit_button("Consultar")

    if submitted:
        response = generate_response(user_input)
        st.markdown(response)
