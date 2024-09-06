import pandas as pd
from sqlalchemy import create_engine 
import argparse

YELLOW_TAXI_TRIP_DATA_FILE_PATH:str = './data/green_tripdata_2019-09.csv'
ZONES_DATA_FILE_PATH:str = './data/zone_lookup.csv'
CHUNK_SIZE = 10000

def main(params) -> None:
  engine = create_db_engine(params=params)
  # load taxi trip data
  print('Loading yellow taxi trip data')
  load_data_in_db(engine, 'yellow_taxi_trip', YELLOW_TAXI_TRIP_DATA_FILE_PATH)

  print('Loading Zones data')
  load_data_in_db(engine, 'zones', ZONES_DATA_FILE_PATH)

def create_db_engine(params):
  return create_engine(f'postgresql://{params.db_user}:{params.password}@{params.host}:{params.port}/{params.db_name}')

def load_data_in_db(engine, table_name:str, file_path:str) -> None:
  with pd.read_csv(file_path, chunksize=CHUNK_SIZE) as reader:
    for chunk in reader:
      chunk.to_sql(name=table_name, con=engine, if_exists='append', index=False)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Data Ingestion Pipeline")
  parser.add_argument('--db_user', type=str, help="Database use login")
  parser.add_argument('--password', type=str, help='Dtabase user pasword')
  parser.add_argument('--db_name', type=str, help='Database name')
  parser.add_argument('--host', type=str , help='Database host')
  parser.add_argument('--port', type=str, help='Database port')

  args = parser.parse_args()
  main(args)