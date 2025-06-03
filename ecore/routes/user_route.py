from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from ecore.service.dependencies import get_db

user_router = APIRouter(prefix='/user', tags=["user"])


@user_router.get("/")
async def root(db: Session = Depends(get_db)):

    query_get_user_by_id = "SELECT * FROM app_user WHERE id_user = 2"
    result = db.execute(text(query_get_user_by_id))
    return result.fetchone(), 200


@user_router.post("/user")
async def health_check():
    # return {"status": "ok"}
    return 405


if __name__ == '__main__':
    db = get_db()
    query_get_user_by_id = "SELECT * FROM app_user WHERE id_user = 2"
    result = db.execute(text(query_get_user_by_id))
    print(result.fetchone())