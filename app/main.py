from fastapi import FastAPI
from app.routes.health import router as health_router

app = FastAPI(title="Personal Agent Backend")

app.include_router(health_router)

@app.get("/")
def root():
    return {"message": "Personal Agent API running"}