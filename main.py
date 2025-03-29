from fastapi import FastAPI
from api.analyse import router as analyse_router

app = FastAPI()

app.include_router(analyse_router, prefix="/analyse")

@app.get("/")
def root():
    return {"message": "Bienvenue sur l'API d'analyse technique"}
