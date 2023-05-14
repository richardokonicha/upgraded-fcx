from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from tgbot.models.model import Base
# 
# from .model import Base

DB_FILE_PATH = 'tgbot/models/database.db'
SQLITE_URL = f'sqlite:///{DB_FILE_PATH}'
engine = create_engine(SQLITE_URL, echo=True, connect_args={'check_same_thread': False})

Session = sessionmaker(bind=engine)
session = Session()

def create_tables():
    Base.metadata.create_all(engine)

class Database:
    def __init__(self):
        self.session = session

    def commit(self):
        self.session.commit()




