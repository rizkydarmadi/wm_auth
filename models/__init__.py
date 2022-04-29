from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import (
    POSTGRESQL_USER, POSTGRESQL_PASSWORD, POSTGRESQL_HOST, 
    POSTGRESQL_DATABASE, POSTGRESQL_PORT
)

# Create sqlalchemy session
username = POSTGRESQL_USER
password = POSTGRESQL_PASSWORD
host = POSTGRESQL_HOST
port = POSTGRESQL_PORT
database = POSTGRESQL_DATABASE

engine = create_engine(
        f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
        , pool_size=20, max_overflow=0, pool_timeout=300
    )
Session = sessionmaker(engine, future=True)
Base = declarative_base()

# for alembic automigrations
from models.user import User