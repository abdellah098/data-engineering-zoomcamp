## Docker & SQL

### Docker tags
```
docker run --rm ubuntu
```

Using the **--rm** option with a docker run command automatically remove the container and its associated anonymous volumes when it exits.
This is useful for containers that you don't need to persist after they have completed their task.

### wheel package version
```
docker run -it python:3.9 bash
```

This command create and starts a new container using python:3.9 image in interactive mode using **bash** command inside the conatiner to start th bash shell


The wheel package version is 0.42.0

### Prepare Postgres
* Downloading CSV files
  The yellow taxi trip and zone data are download and put in data/

  To download the zone lookup data you can use this command
  wget https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv

  > Running this command on mac throw certificate check error, to resolve the issue.
  You can use --no-check-certificate  option.

  ```wget https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv --no-check-certificate```

* Data ingestion script
The yellow taxi trip and zones data are putting in postgres using a script.

  By following these steps, you can run the script in a Docker container and visualize data with pgAdmin.

  1: Create the ingestion script docker image
  ```
  docker build -t ingest:v01 .
  ```
  2: Create a postgres database in docker container 
  ```
  docker run -d --name pg_database \
  -e POSTGRES_USER=root \
  -e POSTGRES_PASSWORD=root \
  -e POSTGRES_DB="taxi_trip" \
  -v data_folder_absolute_path:/var/lib/postgresql/data \
  --network=data_ingestion_network \
  -p 5432:5432 \
  postgres:13
  ```
  3: Running pgadmin in docker container
  ```
  docker run -d \
    --name pg_admin \
    -e 'PGADMIN_DEFAULT_EMAIL=root.dev@gmail.com' \
    -e 'PGADMIN_DEFAULT_PASSWORD=root' \
    -p 80:80 \
    --network data_ingestion_network \
    dpage/pgadmin4
    ```
  4: Running the data ingestion script in docker container to put data in posgtres database
  ```
  docker run -it \
  --network=data_ingestion_network \
  taxi_ingest:v01 --db_user=root --password=root --db_name=taxi_trip --host=pg_database --port=5432
  ```


