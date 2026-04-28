# 🚀 User Service (Microservice com FastAPI)

Microserviço simples de usuários desenvolvido em Python utilizando FastAPI, com estrutura organizada e preparado para execução com Docker.

---

## 📌 Objetivo

Este projeto demonstra:

* Estrutura organizada de microserviço
* Separação de responsabilidades (routers, services, schemas)
* API REST simples
* Uso de variáveis de ambiente
* Containerização com Docker

---

## 🧱 Estrutura do Projeto

```id="lghp4w"
user_service/
 ├── .envs/
 │   ├── .env
 │   ├── .env.example
 │   └── .env.prod
 ├── app/
 │   ├── core/
 │   │   └── config.py
 │   ├── db/
 │   │   └── database.py
 │   ├── models/
 │   │   └── models.py
 │   ├── routers/
 │   │   └── routes.py
 │   ├── schemas/
 │   │   └── schemas.py
 │   ├── services/
 │   │   └── user_service.py
 │   ├── main.py
 │   └── __init__.py
 ├── Dockerfile
 ├── requirements.txt
 └── README.md
```

---

## ⚙️ Tecnologias

* Python 3.10+
* FastAPI
* Uvicorn
* Pydantic / pydantic-settings
* Docker

---

## 📦 Instalação (local)

```bash id="j5zgyk"
git clone https://github.com/MarcosDeveloper-Science/User-Service.git
cd User-Service
```

Criar ambiente virtual:

```bash id="x5svwf"
python -m venv venv
venv\Scripts\activate
```

Instalar dependências:

```bash id="d04cdw"
pip install -r requirements.txt
```

---

## 🔐 Variáveis de Ambiente

Arquivo utilizado:

```id="8r4q48"
.envs/.env
```

Exemplo:

```id="goxvqs"
APP_NAME="User Service"
DEBUG=True
```

---

## ▶️ Executando localmente

```bash id="9fh5hv"
uvicorn app.main:app --reload
```

Acesse:

👉 http://127.0.0.1:8000/docs

---

## 🐳 Executando com Docker

### Build

```bash id="7x8yxf"
docker build -t user-service .
```

---

### Run

```bash id="gl5fuy"
docker run -p 8000:8000 user-service
```

---

## 📡 Endpoints

### Criar usuário

```id="k6ndhx"
POST /users/
```

Body:

```json id="80w0gj"
{
  "name": "Marcos"
}
```

---

### Listar usuários

```id="fhjcib"
GET /users/
```

---

## 🧠 Arquitetura

O projeto segue separação por camadas:

* **routers** → camada HTTP (entrada da API)
* **services** → regra de negócio
* **schemas** → validação de dados
* **models** → estrutura interna
* **db** → persistência (fake)
* **core** → configurações

---

## ⚠️ Observações

* Banco em memória (`fake_db`)
* Projeto voltado para estudo
* Estrutura pronta para evoluir para microserviços reais

---

## 🔥 Próximos Passos

* Adicionar banco real (PostgreSQL)
* Criar outro microserviço (ex: Order Service)
* Comunicação entre serviços (HTTP)
* Docker Compose

---

## 👨‍💻 Autor

Projeto desenvolvido para estudo de microserviços com Python.
