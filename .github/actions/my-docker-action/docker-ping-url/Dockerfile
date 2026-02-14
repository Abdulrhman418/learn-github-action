FROM python:3.11-alpine3.19

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY main.py .

ENTRYPOINT ["python", "/app/main.py"]
