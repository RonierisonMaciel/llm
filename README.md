# 🏦 BDI - Banco de Dados Intelligence

Este projeto utiliza o **GPT4All** para interpretar e responder perguntas sobre um banco de dados SQLite. Ele permite que os usuários consultem informações de forma natural, sem precisar escrever SQL manualmente.

---

## **📌 Como configurar o projeto para rodar localmente em sua máquina**

### **1️⃣ Clonar o repositório**
```bash
git clone https://github.com/ronierisonmaciel/llm.git
cd llm
```

---

## **📌 Instalando o GPT4All**
O projeto utiliza o **GPT4All** para processar as consultas. Siga os passos abaixo para instalar corretamente:

### **1️⃣ Baixar e instalar o GPT4All**
- 🔗 Acesse: [https://gpt4all.io/index.html](https://gpt4all.io/index.html)
- 📥 Baixe a versão correspondente ao seu sistema operacional (Windows, macOS ou Linux)
- 🛠 Instale e abra o aplicativo para verificar se está funcionando corretamente

### **2️⃣ Baixar o modelo LLM**
O projeto está configurado para usar o modelo **Nous-Hermes-2-Mistral-7B-DPO**, mas você pode escolher outro compatível.
- 🔗 Acesse: [https://gpt4all.io/models](https://gpt4all.io/models)
- 📥 Baixe o modelo **Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf**
- 🔀 Mova o modelo para a pasta de modelos do GPT4All, normalmente localizada em:
  - **Windows:** `C:\Users\seu_usuario\AppData\Local\nomic.ai\GPT4All`
  - **macOS:** `~/Library/Application Support/nomic.ai/GPT4All/`
  - **Linux:** `~/.local/share/nomic.ai/GPT4All/`

> **Nota:** O caminho exato pode variar. Certifique-se de copiar corretamente o modelo para a pasta apropriada.

---

## **📌 Configuração do projeto**

### **1️⃣ Criar um arquivo `.env` com suas configurações locais**
Crie um arquivo `.env` baseado no exemplo existente no repositório:
```bash
cp .env.example .env
```

✏️ **Edite o `.env` conforme necessário**, definindo:
- O **caminho do banco de dados**
- O **caminho do modelo GPT4All**

#### **Exemplo do `.env`**
```ini
# Caminho do banco de dados (altere conforme necessário)
DB_PATH=meu_banco_local.db

# Caminho do modelo GPT4All (altere conforme necessário)
MODEL_PATH=/Users/seu_usuario/Library/Application Support/nomic.ai/GPT4All/Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf
```

No Windows:
```powershell
notepad .env
```
No Linux/macOS:
```bash
nano .env
```

---

## **📌 Instalando as dependências**
O projeto requer **Python 3.8 ou superior** e as bibliotecas do GPT4All e Streamlit.

### **1️⃣ Criar e ativar um ambiente virtual (opcional, mas recomendado)**
#### **Windows (PowerShell)**
```powershell
python -m venv venv
venv\Scripts\Activate
```

#### **macOS/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### **2️⃣ Instalar as dependências**
```bash
pip install -r requirements.txt
```

---

## **📌 Executando o projeto**
Após configurar o `.env` e instalar as dependências, execute:

```bash
streamlit run app.py
```

A aplicação abrirá no seu navegador com a interface do **BDI - Banco de Dados Intelligence**.

---

## **📌 Como funciona?**
1. O usuário faz perguntas sobre o banco de dados, como:
   ```
   Qual foi o último valor do IPCA em Recife?
   ```
2. O modelo consulta o banco de dados e responde de forma clara e objetiva.
3. As respostas são armazenadas em cache para melhorar a performance.

---

## **📌 Segurança e Privacidade**
✅ **O banco de dados local e o `.env` NÃO são versionados**, garantindo segurança.  
✅ **Se você precisar de um banco de exemplo, pode disponibilizar um `.db` no repositório.**  

---

## **📌 Contribuições**
Sinta-se à vontade para contribuir! Para sugestões, abra uma **issue** ou envie um **pull request**. Veja como contribuir:

1. **Escolher uma tarefa caso acredite ser pertinente ao projeto**
2. Criar uma nova issue com o título da tarefa (ex: `Tarefa: Dockerizar o projeto`)
3. Criar uma branch com o nome da tarefa (ex: `feature/docker`)
4. Fazer commits claros e bem descritos na branch
5. Ao finalizar, abrir um Pull Request com:
   - Descrição do que foi feito
   - Como testar
   - Prints se necessário

Se precisar de suporte, entre em contato na aba discussões. 🐧
