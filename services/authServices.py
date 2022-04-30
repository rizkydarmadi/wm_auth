from repository.authRepository import authRepository
from common.responses_services import BadRequest,Created,InternalServerError, Ok
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm
from common.security import generate_jwt_token_from_user
from settings import JWT_PREFIX
from models.user import User


class AuthServices:

    @staticmethod
    async def get_all(requestUser:User,limit:int,terms:str):
        data, numdata = authRepository.get_all(limit=limit,terms=terms)
        return Ok(data={
            'count':numdata,
            'results':[{
                'username':item.username,
                'name':item.name,
                'email':item.email

            }for item in data]
        })
    
    @staticmethod
    async def sign_up(request):
        
        # get all request
        username = request.username
        name = request.name
        password = request.password
        email = request.email

        # check if username is exist
        if authRepository.check_user(user=username) != False:
            return BadRequest(message='username already exist')
        
        # check if email is exist
        if authRepository.check_email(email=email) != False:
            return BadRequest(message='email already exist')

        #hashed password
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        password_hashed = pwd_context.hash(password)

        # create new user
        new_user = authRepository.create_new_user(username=username,name=name,password=password_hashed,email=email)

        return Created(data={
            'username':new_user.username,
            'email':new_user.email
        })


    # For Open Api Login
    @staticmethod
    async def generate_token(form_data: OAuth2PasswordRequestForm):
        try:
        
            # check is user exist on database
            if authRepository.check_user(form_data.username) != True:
                return BadRequest(message="username not found")

            # check is password correct
            if authRepository.verify_password(user=form_data.username,plain_password=form_data.password) != True:
                return BadRequest(message="invalid password")

            # Generate JWT Token for user
            user = authRepository.get_user(form_data.username)
            jwt_token = await generate_jwt_token_from_user(user=user)

            return Ok(data={"access_token": jwt_token, "token_type": JWT_PREFIX})
        except Exception as e:
            return InternalServerError(error=str(e))


