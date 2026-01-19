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
@click.option('--table', default='zone_lookup', help='Target table name')

def ingest_data(user, password, host, port, db, table):
    # Ingestion logic here
    prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc'
    url = f"{prefix}/taxi_zone_lookup.csv"
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df = pd.read_csv(url)
    df.to_sql(
                name=table,
                con=engine,
                if_exists='replace'
            )
if __name__== '__main__':
    ingest_data()