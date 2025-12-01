# 🐳 Load Balancer com NGINX e Flask (Docker Compose)

Este projeto demonstra como configurar um balanceamento de carga Round-Robin simples para uma aplicação Flask utilizando **Docker** e **NGINX**.

## 🎯 Arquitetura do Projeto

O ambiente é composto por três serviços coordenados pelo Docker Compose:

1.  **Backend (app1 e app2):** Duas instâncias idênticas da aplicação Flask rodando na porta `5000`.
2.  **Load Balancer (nginx):** Um container NGINX que atua como **Gerente de Tráfego**, distribuindo as requisições que chegam na porta `8080` para os backends de forma alternada (Round-Robin).
3.  **Rede:** Uma rede interna do Docker permite que o NGINX se comunique com os backends usando seus nomes de serviço (`app1` e `app2`).

## 🛠️ Pré-requisitos

Para rodar este projeto, você precisa ter o seguinte instalado em seu sistema (Windows 11):

* **[Docker Desktop](https://www.docker.com/products/docker-desktop/)**: Necessário para rodar o motor Docker e o comando `docker compose`.
* **Python 3**: Necessário para rodar o script de teste `client.py` localmente.
* **Biblioteca `requests`**: Instale-a no seu ambiente Python local:
    ```bash
    pip install requests
    ```

## 📁 Estrutura de Arquivos

Certifique-se de que sua pasta de projeto contenha os seguintes arquivos:

| Arquivo | Propósito |
| :--- | :--- |
| `app.py` | O código Flask que retorna o nome do container. |
| `Dockerfile` | A receita para construir a imagem Python do backend. |
| `nginx.conf` | O arquivo de configuração do NGINX, definindo o `upstream` e o `proxy_pass`. |
| `docker-compose.yml` | O orquestrador que sobe 2 apps + NGINX e configura os **healthchecks**. |
| `client.py` | O script Python que simula requisições para testar o balanceamento. |

## 🚀 Instruções de Setup e Execução

Siga os passos abaixo no seu terminal (PowerShell, CMD ou Terminal do VS Code):

### 1. Construir e Iniciar o Ambiente

Este comando constrói a imagem do backend e inicia todos os serviços definidos no `docker-compose.yml`.

```bash
docker compose up --build
