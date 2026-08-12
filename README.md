# API Connect - Gerenciamento de Usuários

Projeto desenvolvido na disciplina de Desenvolvimento Back-end com o objetivo de criar uma API REST para gerenciamento de usuários.

## Objetivo

A API permite realizar operações CRUD de usuários, possibilitando cadastrar, listar, buscar, atualizar e remover registros.

Os dados são armazenados temporariamente em memória para simular uma camada de persistência durante o desenvolvimento do MVP.

## Tecnologias utilizadas

- Python
- Flask
- JSON
- HTTP
- Thunder Client
- Git
- GitHub

## Estrutura do projeto

```text
api-connect/
├── controllers/
│   └── usuario_controller.py
├── data/
│   └── usuarios.py
├── routes/
│   └── usuario_routes.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```
## Como executar o projeto

Clone o repositório:

```bash
git clone https://github.com/evellyngois/api-connect-evellyn-gois.git
```

Entre na pasta do projeto:

```bash
cd api-connect-evellyn-gois
```

Crie o ambiente virtual:

```bash
python -m venv venv
```

Instale as dependências:

```bash
venv\Scripts\python.exe -m pip install -r requirements.txt
```

Execute a aplicação:

```bash
venv\Scripts\python.exe app.py
```

O servidor será iniciado em:

```text
http://127.0.0.1:5000
```

## Endpoints da API

| Método | Endpoint | Função | Status de sucesso |
|---|---|---|---|
| GET | `/usuarios` | Listar todos os usuários | 200 |
| GET | `/usuarios/<id>` | Buscar usuário pelo ID | 200 |
| POST | `/usuarios` | Cadastrar usuário | 201 |
| PUT | `/usuarios/<id>` | Atualizar usuário | 200 |
| DELETE | `/usuarios/<id>` | Remover usuário | 204 |

## Exemplo de cadastro

### POST `/usuarios`

Corpo da requisição:

```json
{
  "nome": "Mariana Costa",
  "email": "mariana@email.com"
}
```

Resposta:

```json
{
  "data": {
    "id": 3,
    "nome": "Mariana Costa",
    "email": "mariana@email.com"
  }
}
```

Status HTTP:

```text
201 Created
```

## Validação de dados

Os campos `nome` e `email` são obrigatórios.

Exemplo de requisição inválida:

```json
{
  "nome": "Usuário sem e-mail"
}
```

Resposta:

```json
{
  "error": "O campo e-mail é obrigatório."
}
```

Status HTTP:

```text
400 Bad Request
```

## Códigos HTTP utilizados

- `200 OK`: operação realizada com sucesso.
- `201 Created`: usuário criado com sucesso.
- `204 No Content`: usuário removido com sucesso.
- `400 Bad Request`: dados da requisição inválidos.
- `404 Not Found`: usuário não encontrado.

## Organização da aplicação

O projeto utiliza separação de responsabilidades:

- `routes`: definição dos endpoints e métodos HTTP.
- `controllers`: processamento das requisições e lógica da aplicação.
- `data`: armazenamento temporário dos usuários em memória.
- `app.py`: inicialização e configuração do servidor Flask.

## Testes

Os endpoints foram testados manualmente utilizando o Thunder Client no Visual Studio Code.

Foram validados cenários de sucesso e falha, incluindo os códigos HTTP `200`, `201`, `400` e `404`.

## Autor

Evellyn Gois

Projeto acadêmico desenvolvido para a disciplina de Desenvolvimento Back-end.