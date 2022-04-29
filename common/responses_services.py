from typing import Any, Optional, Union

from fastapi.responses import JSONResponse

class Ok():
    def __init__(self, data:Optional[Any]) -> None:
        if data != None:
            self.data = data
        else:
            self.data = ''

    def json(self):
        '''
        parse class to JSONReponse
        '''
        return JSONResponse(content=self.data, status_code=200)

class Created():
    def __init__(self, data:Optional[Any]) -> None:
        if data != None:
            self.data = data
        else:
            self.data = ''

    def json(self):
        '''
        parse class to JSONReponse
        '''
        return JSONResponse(content=self.data, status_code=200)

class NoContent():

    def __init__(self) -> None:
        self.data = ''

    def json(self)->JSONResponse:
        '''
        parse class to JSONReponse
        '''
        return JSONResponse(content=self.data, status_code=204)

class Unauthorized():

    def __init__(self, custom_response:str=None) -> None:
        self.custom_response = custom_response

    def json(self)->JSONResponse:
        if self.custom_response == None:
            return JSONResponse(content={'message': 'Unauthorized'}, status_code=401)
        return JSONResponse(content=self.custom_response, status_code=401)

class BadRequest():

    def __init__(self, message:str=None, custom_response:Optional[Any]=None) -> None:
        '''
        message: bad request message, for default json response
        custom_response: override default json response
        default json response:
        json:{
            'message': f'{message}'
        }
        status_code: 400
        '''
        self.custom_response = None
        if custom_response == None:
            self.message = message
        else:
            self.custom_response = custom_response

    def json(self) -> JSONResponse:
        '''
        parse class to JSONReponse
        '''
        if self.custom_response == None:
            return JSONResponse(content={'message': self.message}, status_code=400)
        else:
            return JSONResponse(content=self.custom_response, status_code=400)

class Forbidden():

    def __init__(self, custom_response:Optional[Any]=None) -> None:
        '''
        custom_response: override default json response
        default json response:
        json:{
            'message': 'You don\'t have permissions to perform this action'
        }
        status_code: 403
        '''
        self.custom_response = None
        if custom_response == None:
            self.message = 'You don\'t have permissions to perform this action'
        else:
            self.custom_response = custom_response

    def json(self)->JSONResponse:
        '''
        parse class to JSONReponse
        '''
        if self.custom_response == None:
            return JSONResponse(content={'message': self.message}, status_code=403)
        else:
            return JSONResponse(content=self.custom_response, status_code=403)

class NotFound():

    def __init__(self, message:str='Not Found', custom_response:Optional[Any]=None) -> None:
        '''
        custom_response: override default json response
        default json response:
        json:{
            'message': 'Not Found'
        }
        status_code: 404
        '''
        self.custom_response = None
        if custom_response != None:
            self.custom_response = custom_response
        else:
            self.message = message

    def json(self)->JSONResponse:
        '''
        parse class to JSONReponse
        '''
        if self.custom_response == None:
            return JSONResponse(content={'message': self.message}, status_code=404)
        else:
            return JSONResponse(content=self.custom_response, status_code=404)
    
class InternalServerError():

    def __init__(self, error:str=None, custom_response:Optional[Any]=None) -> None:
        '''
        error: error string for defaut json response
        custom_response: override default json response
        default json response:
        json:{
            'error': '{error}'
        }
        status_code: 500
        '''
        self.custom_response = None
        if custom_response != None:
            self.custom_response = custom_response
        else:
            self.error = error

    def json(self)->JSONResponse:
        '''
        parse class to JSONReponse
        '''
        if self.custom_response == None:
            return JSONResponse(content={'error': self.error}, status_code=500)
        else:
            return JSONResponse(content=self.custom_response, status_code=500)
    
def common_response(res:Union[Ok, Created, NoContent, BadRequest, Unauthorized, Forbidden, NotFound, InternalServerError])->JSONResponse:
    return res.json()
