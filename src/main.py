""" A FastAPI application for Hereicom. """

from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """ Returns hello world on root path. """
    return {"Hello": "World!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q_param: Optional[str] = None):
    """ Querry item with a parameter. """
    return {"item_id": item_id, "q_param": q_param}
