# Usa imagem base do Python 3.13.3 (slim = mais leve)
FROM python:3.13.3-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia o arquivo de dependências para o container
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos da aplicação
COPY . .

# Expõe a porta que o Flask vai usar (por padrão 5000)
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
