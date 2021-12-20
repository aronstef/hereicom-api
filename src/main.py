""" A FastAPI application for Hereicom. """

from fastapi import FastAPI

from api import api_router

app = FastAPI()


app.include_router(api_router, prefix="/api")
