import os
from dotenv import load_dotenv

# 📌 Carregar configurações do `.env`
load_dotenv()

modelo_path = os.getenv(
    "MODEL_PATH"
)
