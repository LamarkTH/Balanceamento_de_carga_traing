import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    container_name = os.getenv('CONTAINER_NAME', 'Desconhecido')
    return f"Olá! Resposta vinda do container: {container_name}\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)