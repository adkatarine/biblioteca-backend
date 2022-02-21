# Sistema de gerenciamento de uma biblioteca

Desenvolvimento do [challenge](README.devchallenge-io.md) de um sistema de gerenciamento de uma biblioteca da [Devchallenge](https://www.devchallenge.com.br).

## 🚀 Começando
Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### 📋 Pré-requisitos

De que coisas você precisa para instalar o software e como instalá-lo?
Primeiro, clone este projeto em sua máquina, crie um ambiente virtual e ative. Feito isso, execute o seguinte comando para instalar todas as suas dependências:

```
pip install -r requirements.txt
```

Caso queira fazer melhorias ou alterações no projeto, execute este comando:
```
pre-commit install
```

Após isso, crie um arquivo .env e insira estas três variáveis com suas respectivas informações:
```
export CONNECTION_URL = insira a conexão com o database
export DATABASE = insira o nome do database
export COLLECTION = insira o nome da coleção
```

Agora você já pode executar este ultimo comando para iniciar a aplicação:
```
uvicorn src.server:app --reload
```

## 📩 Rotas da aplicação:

[POST] /obras : A rota deverá receber titulo, editora, foto e autores no seguinte formato: {"title": "Harry Potter", "publishing_company": "Rocco", "photo": "https://i.imgur.com/UH3IPXw.jpg", "authors": ["JK Rowling", "..."]}

[GET] /obras/ : A rota deverá listar todas as obras cadastradas

[PUT] /obras/🆔 : A rota deverá atualizar as informações de titulo, editora, foto e autores da obra com o id presente nos parâmetros da rota

[DELETE] /obras/🆔 : A rota deverá deletar a obra com o id presente nos parâmetros da rota

## 🛠️ Estrutura do projeto
```
biblioteca-backend
├── src/
│   ├── __init__.py
│   ├── server.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── database.py
│   ├── infra/
│   │   ├── __init__.py
│   │   ├── helper/
│   │   │   ├── __init__.py
│   │   │   └── helper.py
│   │   └── mongodb/
│   │       ├── __init__.py
│   │       ├── config/
│   │       |   ├── __init__.py
│   │       |   └── database.py
│   │       └── repositories/
│   │           ├── __init__.py
│   │           └── repository_work.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── route_work.py
│   └── schemas/
│       ├── __init__.py
│       └── work.py
├── venv/
├── .env
├── .flake8
├── .gitignore
├── .pre-commit-config.yaml
├── .pylint
├── README.devchallenge-io.md
├── README.md
└── requirements.txt
```

## 🚧 Construído com

Ferramentas utilizadas para o desenvolvimento deste projeto:

* [FastAPI](https://fastapi.tiangolo.com) - Framework
* [MongoDB](https://docs.mongodb.com) - Database
* [Pylint](https://pypi.org/project/pylint/) - Ferramenta de análise de código estático do Python