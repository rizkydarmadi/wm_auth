from sqlalchemy import Column, Integer, String,DateTime,Boolean
from models import Base

class User(Base):
    __tablename__ = 'user'

    username = Column('username',String(length=50),primary_key=True,nullable=False)
    name = Column('nama', String(length=75),nullable=False)
    password = Column('password',String(length=128),nullable=False)
    email = Column('email',String(length=128),nullable=False)
    join_date = Column('join_date', DateTime(timezone=True), nullable=False)
    status = Column('status',Boolean)
    deleted_at = Column('deleted_at', DateTime(timezone=True))


