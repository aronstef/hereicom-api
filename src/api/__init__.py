from fastapi import APIRouter

from api.endpoints import apikey, login, users, lora

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(apikey.router, prefix="/apikeys", tags=["apikeys"])
api_router.include_router(lora.router, prefix="/lora", tags=["lora"])
