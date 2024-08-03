from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base , sessionmaker

engine = create_engine('sqlite:///contatos.db', echo=True)

Base = declarative_base()

