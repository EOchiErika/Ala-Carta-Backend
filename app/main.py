from fastapi import FastAPI #Trae la erramienta principal de fastapi
from app.modules.users.router import router as users_router

app = FastAPI() #crea la app

app.include_router(users_router) #conecta el router a la app

@app.get("/") #lo que se va a mostrar si se ingresa a la raiz del sistema
def root():
    return {"message": "ALa Carta"}
