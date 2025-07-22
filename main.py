from fastapi import FastAPI
from routes import boletos

app = FastAPI()

app.include_router(boletos.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}