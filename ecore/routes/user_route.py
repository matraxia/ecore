from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from ecore.service.dependencies import get_db
import ecore.auth.auth_handler as auth

user_router = APIRouter(prefix='/user', tags=["user"])


@user_router.get("/")
async def root(db: Session = Depends(get_db)):

    query_get_user_by_id = "SELECT * FROM users"
    result = db.execute(text(query_get_user_by_id))
    return str(result.fetchall()), 200 #il risultato di fetchall va probabilmente formattato prima di essere mandato


@user_router.post("/user")
async def health_check():
    # return {"status": "ok"}
    return 405

@user_router.get("/login")
async def login(token):
    if(auth.decode_jwt(token)):
        return 200
    else: 
        return 404

@user_router.post("/signup")
async def login():
    return 405