from fastapi import APIRouter

from .files import router as files_router
from .tasks import router as tasks_router

router = APIRouter(prefix="/api")
router.include_router(files_router)
router.include_router(tasks_router)
