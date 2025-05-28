from fastapi import APIRouter

user_router = APIRouter(prefix='user/')


@user_router.get("/")
async def root():
    return "user", 200


@user_router.post("/user")
async def health_check():
    # return {"status": "ok"}
    return 405