# Dockerfile

# 1. Começamos com uma imagem base leve do Python
FROM python:3.9-slim

# 2. Definimos a pasta de trabalho dentro do container
WORKDIR /app

# 3. Instalamos o Flask e o curl (necessário para testes de saúde depois)
# O flag -y confirma a instalação automaticamente
RUN pip install flask && apt-get update && apt-get install -y curl

# 4. Copiamos o arquivo app.py da sua máquina para o container
COPY app.py .

# 5. Avisamos que o container usa a porta 5000
EXPOSE 5000

# 6. O comando que roda quando o container inicia
CMD ["python", "app.py"]