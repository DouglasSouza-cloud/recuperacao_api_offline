# Consumidor API offline

A API deve ser instalada localmente antes de iniciar o desenvolvimento da aplicação consumidora. Para isso, é necessário ter o Python e o Git instalados no computador.


# INSTALAÇÃO DA API OFFLINE:

# Etapa 1 — Clonar o repositório
Abra o terminal e execute:
git clone https://github.com/jpsvalentim/api-meteorologica-offline.git

# Etapa 2 — Acessar a pasta do projeto
cd api-meteorologica-offline

# Etapa 3 — Criar o ambiente virtual
python -m venv .venv

# Etapa 4 — Ativar o ambiente virtual
No Windows, utilizando PowerShell:
.\.venv\Scripts\Activate.ps1

# Etapa 5 — Instalar as dependências
pip install -r requirements.txt
Esse comando instala as bibliotecas necessárias para executar a API, conforme especificado no arquivo requirements.txt do repositório.

# Etapa 6 — Executar a API
uvicorn app.main:app --reload

Após ser feita todas as etapas para instalação da api offline, passará para a instalação do consumidor da api offline.


# INSTALAÇÃO DO CONSUMIDOR DA API OFFLINE:

# Etapa 1 — Clonar o repositório
Abra o terminal e execute:
git clone https://github.com/DouglasSouza-cloud/recuperacao_api_offline.git

# Etapa 2 — Acessar a pasta do projeto
Ainda no terminal rode:
cd recuperacao_api_offline

# Etapa 3 — Criar e Ativar o Ambiente virtual
No terminal execute:
python -m venv .venv

Depois:
.\.venv\Scripts\Activate.ps1

# Etapa 5 — Instalar as dependências
Abra o terminal e coloque:
pip install -r requirements.txt

# Etapa 6 — Executar a API
ATENÇÃO - INTERFACE STREAMLIT PODE APRESENTAR FALHAS.

Para rodar a interface Streamlit execute no terminal:
python -m streamlit run frontend.py

Caso o mesmo apresente falhas execute:
python consumidor.py