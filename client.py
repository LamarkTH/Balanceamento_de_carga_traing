import time
import requests

RODADAS = 15

print(f"--- Iniciando Teste de Carga no NGINX (Total de {RODADAS} requisições) ---")
print(f"Alvo: http://localhost:8080")

try:
    for i in range(1, RODADAS + 1):
        response = requests.get('http://localhost:8080')
        print(f"Requisição {i:02}: {response.text.strip()}")
        time.sleep(0.3)
        
except requests.exceptions.ConnectionError:
    print("\n🚨 ERRO: Não foi possível conectar ao Load Balancer (http://localhost:8080).")
    print("Verifique se o 'docker compose up' foi executado e se o NGINX está rodando.")