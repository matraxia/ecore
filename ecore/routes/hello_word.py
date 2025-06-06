from fastapi import APIRouter

hello_word_router = APIRouter()


@hello_word_router.get("/")
async def root():
    return "ecore", 200
