from fastapi import FastAPI
from app.api.routes import register_routes

app = FastAPI()

register_routes(app)


@app.get("/")
def root():
    return {"message": "Ala Carta"}
