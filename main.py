from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from settings import CORS_ALLOWED_ORIGINS
from api.auth import auth_router

app = FastAPI(title='Title FastAPI')
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
@app.get("/")
async def hello():
    return {'Hello': "You Make Me Happy :{) "}