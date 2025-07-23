from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import boletos

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)

app.include_router(boletos.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}