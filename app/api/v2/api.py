"""
API v2 router
"""
from fastapi import APIRouter

api_router = APIRouter()

@api_router.get("/")
async def root():
    return {"message": "API v2 - Coming Soon"}
