from fastapi import FastAPI
from backend import api_v1

app = FastAPI()

app.include_router(api_v1.api_router, prefix="/api/v1")