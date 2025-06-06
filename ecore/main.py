from fastapi import FastAPI
from ecore.routes.hello_word import hello_word_router
from ecore.routes.swap_route import swap_router

app = FastAPI()

app.include_router(hello_word_router)
app.include_router(swap_router)
