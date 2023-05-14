from .model import Base, User, Admin, Transaction
from .database import create_tables, Database

# Create database tables
create_tables()

# Create an instance of the Database class
db = Database()

