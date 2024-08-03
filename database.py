from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base , sessionmaker

engine = create_engine('sqlite:///contatos.db', echo=True)

Base = declarative_base()

class Contato(Base):
    __tablename__ = 'contatos'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    celular = Column(String(20), nullable=False)
    celular_alt = Column(String(20), nullable=True)
    tags = Column(String(100), nullable=True)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

