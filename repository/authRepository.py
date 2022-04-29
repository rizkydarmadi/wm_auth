from models.user import User
from sqlalchemy import select
from models import Session
import pytz
from datetime import datetime



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

