from fastapi import APIRouter, Depends

from src.services.tasks import TaskService
from src.models import Task, ActiveTasks

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("", response_model=ActiveTasks)
async def get_current_tasks_cnt(
    service: TaskService = Depends(),
):
    return service.get_current_tasks_cnt()


@router.get("/{task_id}", response_model=Task)
async def get_result(
    task_id: str,
    service: TaskService = Depends(),
):
    return service.get_result(task_id)
