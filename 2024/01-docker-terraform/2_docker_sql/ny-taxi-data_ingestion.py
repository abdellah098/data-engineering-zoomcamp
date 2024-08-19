import numpy as np
np.float_ = np.float64
import pandas as pd
from sqlalchemy import create_engine
import argparse
import os

PARTQUET_FILE_EXTENSION = '.parquet'
CSV_FILE_EXTENSION = '.csv'

def ingest_data(params) -> None:
  url = params.url
  if url.endswith(PARTQUET_FILE_EXTENSION):
    ingest_from_parquet(params)
  elif url.endswith(CSV_FILE_EXTENSION):
    ingest_from_csv(params)
  
  else:
    print('Insupported data file format')

def ingest_from_parquet(params) -> None:
  chunk_size = params.chunk_size

  try:
    print('Data processing starts')

    data_file = 'data' + PARTQUET_FILE_EXTENSION
    download_data(url=params.url, filename=data_file)

    df = pd.read_parquet(data_file, engine="fastparquet")

    print(f'The file contains {len(df)} records')

    engine = get_db_engine(params)
    for start in range(0, len(df), chunk_size):
      end = start + chunk_size
      chunk = df[start:end]

      chunk.to_sql(name=params.table_name, con=engine, if_exists='append', index=False)

      print(f'successfuly inserted {len(chunk)} new rows')
    
  except BaseException as e:
    print("An error occurs /n")
    print(e)
  
  finally:
    print('Data processing ends')

def download_data(url: str, filename: str) -> None:
  try:
    os.system(f'wget {url} --no-check-certificate -O {filename}')
  except Exception as e:
      print(f"An error occurred: {e}")
      raise

def get_db_engine(params):
  try:
    return create_engine(f'postgresql://{params.user}:{params.password}@{params.host}:{params.port}/{params.db_name}')
  
  except Exception as e:
    print(f'An error occured: {e}')
    raise

def ingest_from_csv(params) -> None:
  try:
    print('Data processing starts')

    data_file = 'data' + CSV_FILE_EXTENSION
    download_data(params.url, data_file)

    engine = get_db_engine(params)
    with pd.read_csv(data_file, chunksize=params.chunk_size) as reader:
      for chunk in reader:
        chunk.to_sql(name=params.table_name, con=engine, if_exists='append', index=False)

    print(f'{params.url} data are successfuly inserted in database')
    
  except Exception as e:
    print(f'An error occured {e}')
    raise e
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Yellow New York data Ingestion From Parquet file')
  parser.add_argument('--user', type=str, help='Database user name')
  parser.add_argument('--password', type=str, help="Database user password")
  parser.add_argument('--db_name', type=str, help='Database name')
  parser.add_argument('--table_name', type=str, help='Table that holds data')
  parser.add_argument('--host', type=str, help="Database host")
  parser.add_argument('--port', type=str, help='Port')

  parser.add_argument('--url', type=str, help='URL of the data file')
  parser.add_argument('--chunk_size', type=int, help='Data Chunks size')

  args = args = parser.parse_args()

  ingest_data(args)