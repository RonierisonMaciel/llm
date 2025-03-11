# 🧠 Cache do Modelo
@st.cache_resource
def load_model():
    """Carrega o modelo GPT4All apenas uma vez."""
    if not os.path.exists(modelo_path):
        st.error(f"❌ Modelo não encontrado: {modelo_path}")
        return None
    try:
        return GPT4All(modelo_path)
    except Exception as e:
        st.error(f"❌ Erro ao carregar o modelo GPT4All: {str(e)}")
        return None

model = load_model()
if model:
    st.success("✅ Modelo carregado com sucesso!")
