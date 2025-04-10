from fastapi import APIRouter
from .test_route import router as test_router

router = APIRouter(prefix="/api/v1")

router.include_router(test_router, prefix="/test", tags=["Test"])
