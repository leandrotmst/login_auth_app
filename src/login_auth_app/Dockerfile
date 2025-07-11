# src/login_auth_app/Dockerfile
# Use uma imagem base Python oficial
FROM python:3.9-slim-buster

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instala as dependências
RUN pip install --no-cache-dir Flask Flask-SQLAlchemy Werkzeug Flask-Login psycopg2-binary Flask-Migrate

# Copia o código da sua aplicação para o diretório de trabalho
# O '.' aqui se refere ao diretório onde o Dockerfile está (src/login_auth_app)
COPY . /app

# Define a variável de ambiente FLASK_APP
# Agora app.py está diretamente em /app
ENV FLASK_APP=app.py

# Expõe a porta que o Flask vai usar
EXPOSE 5000

# O comando para rodar a aplicação será definido no docker-compose.yml
# CMD ["flask", "run", "--host=0.0.0.0"]
