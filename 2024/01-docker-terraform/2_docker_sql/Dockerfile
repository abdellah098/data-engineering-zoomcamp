FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r ./requirements.txt

COPY  ny-taxi-data_ingestion.py ny-taxi-data_ingestion.py

ENTRYPOINT [ "python", "ny-taxi-data_ingestion.py"]