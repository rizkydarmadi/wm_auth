from ctypes import Union
from typing import Tuple,List
from models.user import User
from sqlalchemy import select,or_,func
from models import Session
import pytz
from datetime import datetime
from passlib.context import CryptContext



class authRepository():

    @staticmethod
    def check_user(user:str)->bool:
        with Session() as session:
            stmt = select(User).where(User.username==user)
            data = session.execute(stmt).scalar()
        if data == None:
            return False
        else:
            return True
    
    @staticmethod
    def check_email(email:str)->bool:
        with Session() as session:
            stmt = select(User).where(User.email==email)
            data = session.execute(stmt).scalar()
        if data == None:
            return False
        else:
            return True
    
    @staticmethod
    def create_new_user(username:str,name:str,password:str,email:str)->User:

        with Session() as session:
            new_user = User(
                username=username,
                name=name,
                password=password,
                email=email,
                join_date=datetime.now(pytz.timezone('Asia/Jakarta')),
                status=True
            )
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
        return new_user
    
    @staticmethod
    def verify_password(user,plain_password):
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        with Session() as session:
            stmt = select(User.password).where(User.username==user)
            hashed_password = session.execute(stmt).scalar()
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_user(user:str)->User:
        with Session() as session:
            stmt = select(User).where(User.username==user)
            user = session.execute(stmt).scalar()
        return user
    
    @staticmethod
    def get_all(limit:int=None,terms:str=None)->Tuple[List[User],int]:
        with Session() as session:
            stmt = select(User)\
                .where(or_(User.name.ilike(f'%{terms}%'),User.username.ilike(f'%{terms}%'),User.email.ilike(f'%{terms}%')))\
                .order_by(User.name.asc())\
                .limit(limit=limit)
            data = session.execute(stmt).scalars().all()

            stmt2 = select(func.count(User.username))\
                .where(or_(User.name.ilike(f'%{terms}%'),User.username.ilike(f'%{terms}%'),User.email.ilike(f'%{terms}%')))
            num_data = session.execute(stmt2).scalar()
        
        return data,num_data

    @staticmethod
    def update_user(username=str,email=str,name=str)->User:
        with Session() as session:
            stmt = select(User).where(User.username==username)
            user = session.execute(stmt).scalar()

            # updated data
            user.username = username
            user.email = email
            user.name = name
            session.commit()

            stmt = select(User).where(User.username==username)
            data = session.execute(stmt).scalar()

        return data
    
    @staticmethod
    def update_user_and_username(username=str,new_username=str,email=str,name=str)->User:
        with Session() as session:
            stmt = select(User).where(User.username==username)
            user = session.execute(stmt).scalar()

            # updated data
            user.username = new_username
            user.email = email
            user.name = name
            session.commit()

            stmt = select(User).where(User.username==new_username)
            data = session.execute(stmt).scalar()

        return data
    
    @staticmethod
    def update_password(username=str,new_password=str)->None:
        with Session() as session:
            stmt = select(User).where(User.username==username)
            user = session.execute(stmt).scalar()

            # updated data
            user.password = new_password
            session.commit()



