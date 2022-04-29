from pydantic import BaseModel

class NoContent(BaseModel):

    pass

class Unauthorized(BaseModel):

    message: str = 'Unauthorized'

class BadRequest(BaseModel):

    message: str

class Forbidden(BaseModel):

    message: str = 'You don\'t have permissions to perform this action'

class NotFound(BaseModel):

    detail: str = 'Not found'

class InternalServerError(BaseModel):

    error: str
