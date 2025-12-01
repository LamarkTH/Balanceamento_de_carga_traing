# app.py
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # Pega o nome do container da variável de ambiente 'CONTAINER_NAME'
    # Se não achar, usa 'Desconhecido'
    container_name = os.getenv('CONTAINER_NAME', 'Desconhecido')
    
    # Retorna a mensagem identificando quem respondeu
    return f"Olá! Resposta vinda do container: {container_name}\n"

if __name__ == "__main__":
    # Roda o servidor acessível externamente (0.0.0.0) na porta 5000
    app.run(host='0.0.0.0', port=5000)