from fastapi import FastAPI
from app.api.routes import register_routes
from app.core.config import settings
from app.modules.users import model
from app.core.database import engine, Base
from sqlalchemy import text

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

register_routes(app)


@app.get("/")
def root():
    return {"message": "Ala Carta"}

@app.get("/config-test")
def config_test():
    return {
        "app_name": settings.APP_NAME,
        "database_url": settings.DATABASE_URL
    }

@app.get("/db-test")
def db_test():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"resultado": result.scalar()}
    