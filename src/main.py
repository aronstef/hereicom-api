""" A FastAPI application for Hereicom. """

from fastapi import FastAPI

from api import api_router

app = FastAPI()


@app.get("/")
def read_root():
    """ Returns hello world on root path. """
    return {"Hello": "World!"}


app.include_router(api_router, prefix="")
