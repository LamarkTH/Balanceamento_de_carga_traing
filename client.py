# client.py
import time
import requests # Requer 'pip install requests' no seu Windows

RODADAS = 15

print(f"--- Iniciando Teste de Carga no NGINX (Total de {RODADAS} requisições) ---")
print(f"Alvo: http://localhost:8080")

try:
    # Loop para simular vários usuários/acessos
    for i in range(1, RODADAS + 1):
        # Acessa o NGINX, que fará o balanceamento
        response = requests.get('http://localhost:8080')
        
        # Imprime a resposta do backend
        print(f"Requisição {i:02}: {response.text.strip()}")
        
        # Pequena pausa
        time.sleep(0.3)
        
except requests.exceptions.ConnectionError:
    print("\n🚨 ERRO: Não foi possível conectar ao Load Balancer (http://localhost:8080).")
    print("Verifique se o 'docker compose up' foi executado e se o NGINX está rodando.")