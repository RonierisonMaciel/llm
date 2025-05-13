import streamlit as st
import time
from rapidfuzz import process

# --- CONFIGURAÇÃO DE PÁGINA ---
st.set_page_config(page_title="HuB‑IA – Assistente Inteligente para Dados Públicos da Fecomércio", layout="wide")

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
        body {
            background-color: #0E1117;
            color: white;
        }
        .stTextInput > div > input {
            font-size: 20px !important;
        }
        .main-title {
            font-size: 40px !important;
            text-align: center;
            font-weight: bold;
            margin-top: 1em;
        }
        .sub-title {
            font-size: 24px !important;
            text-align: center;
            margin-top: 0.5em;
        }
        .placeholder-text {
            font-style: italic;
            color: #ccc;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# --- ESTADO DA SESSÃO ---
if "historico" not in st.session_state:
    st.session_state.historico = []

if "resposta_atual" not in st.session_state:
    st.session_state.resposta_atual = None

if "mostrar_sobre" not in st.session_state:
    st.session_state.mostrar_sobre = False

# --- FUNÇÕES ---
def consultar(pergunta):
    sql_gerado = "SELECT SUM(valor) FROM ipca_7060_recife"
    colunas_validas = ["valor", "ano", "localidade", "ipca_7060_recife"]
    col_corrigida = corrigir_coluna("valorr", colunas_validas)

    resposta = (
        f"O resultado da consulta SQL fornecido é uma única tupla contendo um único valor: (1037.18). "
        f"Esta linha indica que a soma dos valores no conjunto de dados 'ipca_7060_recife' armazena para o indicador IPCA de Recife é 1037.18. "
        f"Esse número, tipicamente, seria usado como uma medida financeira ou econômica específica relacionada à cidade do Recife em Brasil."
    )
    return resposta, sql_gerado

def corrigir_coluna(coluna_gerada, colunas_validas):
    match, score, _ = process.extractOne(coluna_gerada, colunas_validas)
    return match if score > 80 else coluna_gerada

def is_read_only_query(sql):
    return sql.strip().lower().startswith("select")

def typing_effect(text, speed=0.01):
    placeholder = st.empty()
    typed_text = ""
    for char in text:
        typed_text += char
        placeholder.markdown(typed_text)
        time.sleep(speed)

def sugerir_perguntas(pergunta):
    if "ipca" in pergunta.lower():
        return [
            "Qual a média do IPCA em 2023?",
            "Compare o IPCA entre Recife e Salvador.",
            "IPCA variou quanto em janeiro de 2022?"
        ]
    elif "pms" in pergunta.lower():
        return [
            "Qual foi a variação da PMS em São Paulo?",
            "PMS de 2020 a 2023 no Brasil."
        ]
    return []

# --- SIDEBAR ---
with st.sidebar:
    st.title("Menu")
    if st.button("ℹ️ Sobre o HuB‑IA"):
        st.session_state.mostrar_sobre = not st.session_state.mostrar_sobre

    st.markdown("---")

    st.subheader("🕘 Histórico")
    if st.session_state.historico:
        for i, item in enumerate(reversed(st.session_state.historico)):
            if st.button(item['pergunta'], key=f"hist_{i}"):
                st.session_state.resposta_atual = item
    if st.button("🧹 Limpar histórico"):
        st.session_state.historico.clear()
        st.session_state.resposta_atual = None

# --- ÁREA PRINCIPAL ---
st.markdown('<div class="main-title">HuB‑IA – Assistente Inteligente para Dados Públicos da Fecomércio</div>', unsafe_allow_html=True)

if st.session_state.mostrar_sobre:
    st.markdown("## Sobre o HuB‑IA")
    st.markdown("""
    O **HuB‑IA** é um assistente inteligente que traduz perguntas em linguagem natural em consultas SQL sobre dados econômicos públicos.

    Ele utiliza o **LangChain** e **SQLite**, com dados como:

    - 📈 Índice de Preços ao Consumidor Amplo (IPCA)  
    - 🛒 Pesquisa Mensal do Comércio (PMC)  
    - 🏭 Pesquisa Mensal de Serviços (PMS)  
    - 💳 Transações com cartões  

    Desenvolvido pela **Fecomércio** para democratizar o acesso e a interpretação dos dados econômicos.
    """)
    st.stop()

st.markdown('<div class="sub-title">O que você quer saber?</div>', unsafe_allow_html=True)
pergunta = st.text_input("", placeholder="Qual a inflação acumulada em Recife?", label_visibility="collapsed")
submit = st.button("enviar")

# --- PROCESSAMENTO ---
if submit and pergunta.strip():
    resposta, sql = consultar(pergunta)

    if not is_read_only_query(sql):
        st.error("⚠️ Apenas comandos de leitura (SELECT) são permitidos.")
    else:
        registro = {
            "pergunta": pergunta,
            "resposta": resposta,
            "sql": sql
        }
        st.session_state.historico.append(registro)
        st.session_state.resposta_atual = registro

# --- EXIBIÇÃO DA RESPOSTA ---
if st.session_state.resposta_atual:
    typing_effect(st.session_state.resposta_atual["resposta"])
    with st.expander("📄 Ver SQL gerado"):
        st.code(st.session_state.resposta_atual["sql"], language="sql")
    st.markdown("<p class='placeholder-text'>Você pode perguntar por ano, por localidade ou comparar períodos distintos.</p>", unsafe_allow_html=True)

    sugestoes = sugerir_perguntas(st.session_state.resposta_atual["pergunta"])
    if sugestoes:
        st.markdown("### 💡 Sugestões:")
        for s in sugestoes:
            st.markdown(f"- {s}")
