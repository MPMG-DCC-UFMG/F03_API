import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from elasticsearch import Elasticsearch

load_dotenv()

host = os.environ.get('DB_HOST')
port = os.environ.get('DB_PORT')
es_username = os.environ.get('ES_USER_NAME')
es_password = os.environ.get('ES_PASSWORD')
es_host = os.environ.get('ES_HOST')
es_port = os.environ.get('ES_PORT')

# engine = create_engine(f'hive://{username}:{password}@{host}:{port}/{schema}', connect_args={'auth': 'LDAP'})
engine = create_engine(
    f'druid://{host}:{port}/druid/v2/sql?header=true', pool_pre_ping=True)

es = Elasticsearch(f"http://{es_host}:{es_port}",
                   http_auth=(es_username, es_password))

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

async def connect():
    Base.metadata.create_all(bind=engine)

async def close():
    db_session.remove()
