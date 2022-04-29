from pydantic import BaseModel

class signUpRequest(BaseModel):
    username : str
    name : str
    password :str
    email :str