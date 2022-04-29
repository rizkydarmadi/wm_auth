from fastapi import APIRouter
from api.auth.auth import router as auth

auth_router = APIRouter(prefix='/auth')
auth_router.include_router(auth)