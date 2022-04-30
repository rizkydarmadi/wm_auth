from pydantic import BaseModel
from typing import List

class signUpRequest(BaseModel):
    username : str
    name : str
    password :str
    email :str

class signUpResponse(BaseModel):
    username:str
    password:str

class getAllResponsesItems(BaseModel):
    username = str
    name = str
    email = str

class getAllResponses(BaseModel):
    count:int
    results:List[getAllResponsesItems]