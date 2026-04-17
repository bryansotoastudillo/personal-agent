from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.agent import router as agent_router
from app.routes.preview import router as preview_router

app = FastAPI(title="Personal Agent Backend")

app.include_router(health_router)
app.include_router(agent_router)
app.include_router(preview_router)

@app.get("/")
def root():
    return {"message": "Personal Agent API running"}