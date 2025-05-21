from fastapi import FastAPI

from ecore.routes.hello_word import hello_word_router

app = FastAPI()

app.include_router(hello_word_router)
