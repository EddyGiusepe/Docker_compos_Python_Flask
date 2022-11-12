'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
# Link de estudo --> https://docs.docker.com/compose/gettingstarted/
import time

import redis  # Biblioteca que conecta com a base de Dados Redis
from flask import Flask

app = Flask(__name__)

cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    '''Função que conta as visualizações da página WEB'''
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    '''Printa na Interface.'''
    count = get_hit_count()
    return f"Feliz de trabalahar com vocês! Vamos seguir com o estudo de NLP-Transformers.{count}."

@app.route("/rota_eddy", methods=["GET"])
def func():
    '''Mais uma rota para testar'''
    return '<h1>Está foi uma apresentação simples de <font color="blue">docker-compose.yml</font></h1>'

