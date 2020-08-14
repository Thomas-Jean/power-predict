from fastapi import APIRouter

from backend.api import power

api_router = APIRouter()


api_router.include_router(power.router, prefix="/power")