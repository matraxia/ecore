from fastapi import APIRouter

hello_word_router = APIRouter()


@hello_word_router.get("/")
async def root():
    return "ecore", 200


@hello_word_router.get("/health")
async def health_check():
    # return {"status": "ok"}
    return 405