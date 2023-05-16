from .model import Base, User, Admin, Transaction
from .database import Database

db = Database()

db.create_tables()

