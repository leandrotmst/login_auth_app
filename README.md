# 🔐 Sistema de Autenticação com Flask + SQLite + Docker

Este projeto é uma aplicação web simples de autenticação de usuários utilizando Flask e SQLite. Ele permite que usuários se registrem e façam login, armazenando as credenciais de forma segura com hash de senha.

## Funcionalidades

- Registro de novos usuários
- Login de usuários existentes
- Senhas armazenadas com hash (Werkzeug)
- Interface web simples (HTML)
- Banco de dados local SQLite

## Estrutura do Projeto

```
login_auth_app/
├── .env
├── .gitignore
├── src/
│   └── backend/
│       └── app.py
│       └── users.db
│   └── templates/
│       └── index.html
│       └── success.html
│       └── error.html
```

## Como executar

1. Instale as dependências:
   ```
   pip install flask werkzeug
   ```

2. Execute o servidor:
   ```
   python src/backend/app.py
   ```

3. Acesse `http://localhost:5000` no navegador.

## Segurança

- As senhas são armazenadas com hash usando Werkzeug.
- O banco de dados é local e simples, recomendado apenas para testes ou aprendizado.

## Observações

- Este projeto não é uma API REST, mas pode ser adaptado facilmente.
- Não recomendado para produção sem melhorias de segurança e arquitetura.

## Licença

Este projeto é livre para