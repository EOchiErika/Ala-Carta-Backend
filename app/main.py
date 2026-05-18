from fastapi import FastAPI
from app.api.routes import register_routes
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

register_routes(app)


@app.get("/")
def root():
    return {"message": "Ala Carta"}