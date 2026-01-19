import click
import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm


@click.command()
@click.option('--user', default='postgres', help='PostgreSQL user')
@click.option('--password', default='postgres', help='PostgreSQL password')
@click.option('--host', default='localhost', help='PostgreSQL host')
@click.option('--port', default=5433, type=int, help='PostgreSQL port')
@click.option('--db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--table', default='green_taxi_data', help='Target table name')
@click.option('--year', default=2025, type=int, help='year of data')
@click.option('--month', default=11, type=int, help='month of data')
def ingest_data(user, password, host, port, db, table, year, month):
    # Ingestion logic here
    prefix = 'https://d37ci6vzurychx.cloudfront.net/trip-data'
    url = f"{prefix}/green_tripdata_{year}-{month:02d}.parquet"
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df = pd.read_parquet(url)
    df.to_sql(
                name=table,
                con=engine,
                if_exists='replace'
            )
if __name__== '__main__':
    ingest_data()