FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ingest_data.py .
COPY ./data/ ./data/

ENTRYPOINT ["python", "ingest_data.py"]