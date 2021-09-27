import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

username = os.environ.get('DB_USER_NAME')
password = os.environ.get('DB_PASSWORD')
host = os.environ.get('DB_HOST')
port = os.environ.get('DB_PORT')
schema = os.environ.get('DB_SCHEMA')

engine = create_engine(f'hive://{username}:{password}@{host}:{port}/{schema}',
                                    connect_args={'auth': 'LDAP'})

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

async def connect():
    Base.metadata.create_all(bind=engine)

async def close():
    db_session.remove()
