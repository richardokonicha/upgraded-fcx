from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from tgbot.models.model import Base, User, Transaction

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

    def get_user(self, user_id):
        return self.session.query(User).filter_by(user_id=user_id).first()

    def user_exists(self, user_id):
        return self.session.query(exists().where(User.user_id == user_id)).scalar()

    def create_user(self, name, user_id, referral=None, is_new_user=False, is_admin=False):
        new_user = User(name=name, user_id=user_id, referral=referral, is_new_user=is_new_user, is_admin=is_admin)
        self.session.add(new_user)
        self.commit()
        return new_user

    def create_transact(self, user_id, transaction_type, amount, status, balance):
        new_transaction = Transaction(user_id=user_id, transaction_type=transaction_type, amount=amount, status=status, balance=balance)
        self.session.add(new_transaction)
        self.commit()
        return new_transaction



