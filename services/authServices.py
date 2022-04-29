from repository.authRepository import authRepository
from common.responses_services import BadRequest,Created
from passlib.context import CryptContext

class AuthServices:
    
    @staticmethod
    async def sign_up(request):
        
        # get all request
        username = request.username
        name = request.name
        password = request.password
        email = request.email

        # check if username is exist
        if authRepository.check_user(user=username) != False:
            return BadRequest.message('username already exist')
        
        # check if email is exist
        if authRepository.check_email(email=email) != False:
            return BadRequest.message('email already exist')

        #hashed password
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        password_hashed = pwd_context.hash(password)

        # create new user
        new_user = authRepository.create_new_user(username=username,name=name,password=password_hashed,email=email)

        return Created(data={
            'username':new_user.username,
            'email':new_user.email
        })



        
        

