FROM python:3.9-slim

WORKDIR /app

RUN pip install flask && apt-get update && apt-get install -y curl

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]