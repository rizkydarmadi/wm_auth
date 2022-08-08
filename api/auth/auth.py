from fastapi import APIRouter, Depends
from common.responses_schemas import BadRequest, InternalServerError,Forbidden
from schemas.authSchemas import changePasswordRequest, signUpRequest,signUpResponse,getAllResponses,getDetailResponsesItems,updateRequestUser,updateRequestResponse,changePasswordResponse
from services.authServices import AuthServices
from common.responses_services import common_response
from common.security import oauth2_scheme,get_user_from_jwt_token
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse


router = APIRouter(
    tags=['auth']
)

@router.get('/view-users',responses={
    '200': {'model':getAllResponses},
    '403': {'model': Forbidden},
    '500': {'model': InternalServerError},
})
async def get_all_user(limit:int=25,terms:str='',token: str = Depends(oauth2_scheme)):
    user = get_user_from_jwt_token(token)
    result = await AuthServices.get_all(requestUser=user,limit=limit,terms=terms)
    return common_response(result)

@router.get('/view-users/{username}/',responses={
    '200': {'model':getDetailResponsesItems},
    '403': {'model': Forbidden},
    '500': {'model': InternalServerError},
})
async def get_detail(username=str,token: str = Depends(oauth2_scheme)):
    user = get_user_from_jwt_token(token)
    result = await AuthServices.get_detail(requestUser=user,username=username)
    return common_response(result)

@router.put('/edit-users/',responses={
    '200': {'model':updateRequestResponse},
    '403': {'model': Forbidden},
    '500': {'model': InternalServerError},
})
async def update_password(request:updateRequestUser,token: str = Depends(oauth2_scheme)):
    user = get_user_from_jwt_token(token)
    result = await AuthServices.update_user(requestUser=user,request=request)
    return common_response(result)

@router.put('/edit-password/',responses={
    '200': {'model':changePasswordResponse},
    '403': {'model': Forbidden},
    '500': {'model': InternalServerError},
})
async def update_user(request:changePasswordRequest,token: str = Depends(oauth2_scheme)):
    user = get_user_from_jwt_token(token)
    result = await AuthServices.update_password(requestUser=user,request=request)
    return common_response(result)

@router.post('/sign-up',responses={
    '200': {'model':signUpResponse},
    '400': {'model': BadRequest},
    '500': {'model': InternalServerError}
})
async def sign_up(request: signUpRequest):
    result = await AuthServices.sign_up(request)
    return common_response(result)

@router.post('/sign-in',responses={
    '400': {'model': BadRequest},
    '500': {'model': InternalServerError}
})
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    result = await AuthServices.generate_token(form_data)
    return common_response(result)

@router.delete('/delete-user/{username}',responses={
    '200': {'message':'name has been deleted'},
    '403': {'model': Forbidden},
    '500': {'model': InternalServerError},
})
async def delete_user(username:str,token: str = Depends(oauth2_scheme)):
    user = get_user_from_jwt_token(token)
    result = await AuthServices.delete_user(requestUser=user,username=username)
    return common_response(result)