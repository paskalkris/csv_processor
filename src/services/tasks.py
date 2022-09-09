from celery.result import AsyncResult
from celery import states

from src.models import Task, ActiveTasks
from src.worker import celery


class TaskService:
    def get_current_tasks_cnt(self) -> ActiveTasks:
        active_tasks = ActiveTasks()

        active = celery.control.inspect().active()
        if active:
            active_tasks.count = sum(len(task_list) for task_list in active.values())

        return active_tasks

    def get_result(self, task_id: str) -> Task:
        task_async_result = AsyncResult(task_id)

        task = Task(id=task_async_result.id, status=task_async_result.status)

        if task.status == states.SUCCESS:
            task.result = task_async_result.get()

        return task
