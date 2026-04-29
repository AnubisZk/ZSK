from fastapi import APIRouter

from app.api.routes import analysis, climate, health, risk

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(analysis.router, tags=["analysis"])
api_router.include_router(risk.router, tags=["risk"])
api_router.include_router(climate.router, tags=["climate"])
