import json
from fastapi import APIRouter
from common.responses_schemas import BadRequest, InternalServerError
from schemas.authSchemas import signUpRequest
from services.authServices import AuthServices
from common.responses_services import common_response


router = APIRouter(
    tags=['auth']
)


@router.post('/sign-up',responses={
    '400': {'model': BadRequest},
    '500': {'model': InternalServerError}
})
async def sign_up(request: signUpRequest):

    result = await AuthServices.sign_up(request)
    return common_response(result)
