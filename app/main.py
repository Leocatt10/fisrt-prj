from fastapi import FastAPI
from app.db.session import connect_to_mongo, close_mongo_connection
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()

@app.get("/")
def read_root():
    return {"message": "Chào mừng Duy Mạnh đến với Backend Chat Real-time!"}