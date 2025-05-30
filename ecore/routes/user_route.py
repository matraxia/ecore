from fastapi import APIRouter
from ecore.auth.auth_handler import auth

user_router = APIRouter(prefix='/user')

from pydantic import BaseModel

class Login(BaseModel):
    nome: str
    password: str


@user_router.get("/")
async def root():
    return "user", 200


@user_router.post("/user")
async def health_check():
    # return {"status": "ok"}
    return 405

@user_router.get("/login")
async def auth(login:Login):
    auth(login.nome,login.password)
    return login