from decimal import Decimal
from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DECIMAL
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Admin(Base):
    """Admin class"""
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)
    name = Column(String)
    merchant_ID = Column(String)
    merchant_pkey = Column(String)
    merchant_pbkey = Column(String)
    duration_reinvest = Column(Integer)
    daily_profits = Column(DECIMAL(8, 6))

    def __repr__(self):
        return f"Admin {self.name}, {self.user_id}"


class User(Base):
    """User class"""
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)
    name = Column(String, nullable=False)
    language = Column(String)
    referral = Column(String)
    registered_date = Column(String)
    is_new_user = Column(Boolean)
    last_visited = Column(String)
    wallet_address = Column(String)

    account_balance = Column(DECIMAL(8, 6))
    active_investment = Column(DECIMAL(8, 6))
    pending_investment = Column(DECIMAL(8, 6))
    active_reinvestment = Column(DECIMAL(8, 6))
    transactions = relationship("Transaction", uselist=True, backref="user")
    is_admin = Column(Boolean, default=False)

    def __init__(self, user_id, name, referral=None, is_new_user=True, is_admin=False):
        self.user_id = user_id
        self.name = name
        self.referral = referral
        self.is_new_user = is_new_user
        self.is_admin = is_admin
        self.registered_date = datetime.now().isoformat()
        self.account_balance = Decimal()
        self.active_investment = Decimal()
        self.active_reinvestment = Decimal()
        self.pending_investment = Decimal()

    def exists(self):
        return session.query(exists().where(User.user_id == self.user_id)).scalar()

    def set_last_visited(self):
        self.last_visited = datetime.now().isoformat()
        return self.last_visited

    def __repr__(self):
        return f"User {self.name}"


class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    transaction_type = Column(String)
    amount = Column(DECIMAL(8, 6))
    received_amount = Column(DECIMAL(8, 6))
    wallet_address = Column(String)
    date = Column(String)
    start_date = Column(String)
    balance = Column(DECIMAL(8, 6))
    dp_txn_id = Column(String, unique=True)
    dp_address = Column(String)
    dp_address_timeout = Column(Integer)
    dp_qrcode_url = Column(String)
    dp_status = Column(String)
    dp_status_text = Column(String)
    status = Column(String)

    def __init__(
        self,
        user_id,
        transaction_type,
        amount,
        wallet_address=None,
        balance=None,
        status="Pending"
    ):
        self.user_id = user_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.wallet_address = wallet_address
        self.date = datetime.now().isoformat()
        self.start_date = datetime.now().replace(
            day=(datetime.now().day+(7-datetime.now().weekday()))
        ).isoformat()
        self.balance = balance
        self.status = status

    @classmethod
    def get_transactions(cls, user_id):
        transaction = session.query(cls).filter_by(user_id=user_id).all()
        if transaction:
            return transaction
        else:
            return None

    @classmethod
    def get_txn_id(cls, txn_id):
        """get_txn_id"""
        return session.query(Transactions).filter_by(dp_txn_id=txn_id).first()


    def get_start_date(self):
        return datetime.fromisoformat(self.start_date).strftime("%A %d. %B %Y")

    def get_close_date(self):
        close_date = datetime.fromisoformat(self.start_date) + timedelta(days=180)
        return close_date.strftime("%A %d. %B %Y")

    def __repr__(self):
        return f"Transaction {self.user_id} {self.transaction_type} {self.amount}"




 
    # @classmethod
    # def get_user(cls, user_id):
    #     if cls.db.session.query(cls.exists().where(cls.user_id == user_id)).scalar():
    #         return cls.db.session.query(cls).filter_by(user_id=user_id).first()
    #     else:
    #         return None


    # @classmethod
    # def get_user(cls, user_id):
    #     if session.query(exists().where(cls.user_id == user_id)).scalar():
    #         return session.query(cls).filter_by(user_id=user_id).first()
    #     else:
    #         return None

    # @classmethod
    # def get_user_by_id(cls, user_id):
    #     return db.session.query(cls).filter_by(user_id=user_id).first()
