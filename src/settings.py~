# coding=utf8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine_url_example = "postgresql+psycopg2://user:password@host/database"

#Wykorzystywany w danej chwili URL do połączenia z bazą danych
engine_url = "postgresql+psycopg2://@/ilf_json"

engine = create_engine(engine_url)

Session = sessionmaker(bind=engine)
