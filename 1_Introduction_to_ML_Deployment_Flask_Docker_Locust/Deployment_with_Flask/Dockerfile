# Imagem base Python 3.9
FROM python:3.9-slim

# Definimos nosso diretório de trabalho
WORKDIR /app

# Copie o arquivo requirements.txt para dentro do contêiner
COPY requirements.txt requirements.txt

# Instalamos as bibliotecas necessárias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copie o modelo e o código do aplicativo no contêiner
COPY ["loan_catboost_model.cbm", "app.py", "./"] .

# Execute o aplicativo (app) usando gunicorn
ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:8989", "app:app" ]
