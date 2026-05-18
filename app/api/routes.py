from fastapi import FastAPI
from app.modules.users.router import router as users_router

def register_routes(app: FastAPI):
    app.include_router(users_router)