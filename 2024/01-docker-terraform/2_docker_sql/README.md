# New York Taxi Data Ingestion Script

This project sets up a PostgreSQL database, a pgAdmin interface, and services for ingesting New York Taxi trip data and taxi zone lookup data into the database. The setup is defined using `docker-compose` and can be easily deployed using Docker.

## Project Structure

- **PostgreSQL Database:** A PostgreSQL database (`new_york_taxi`) is set up to store the taxi trip data and taxi zone lookup information.
- **pgAdmin:** A web-based administration tool for PostgreSQL databases. It is accessible via `http://localhost:8080`.
- **Data Ingestion Services:**
  - **Yellow Taxi Trip Data Ingestion:** Ingests yellow taxi trip data from a Parquet file into the PostgreSQL database.
  - **Taxi Zones Data Ingestion:** Ingests taxi zone lookup data from a CSV file into the PostgreSQL database.

# Important
The docker image taxi_ingest:v01 must be created before executing the docker-compose up  command

# Image generation
docker build -t taxi_ingest:v01 . 
