FROM python:3.10-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DB_PATH=/data/banco_padrao.db
ENV MODEL_PATH=/models/Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]