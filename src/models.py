from pydantic import BaseModel


class Task(BaseModel):
    id: str
    status: str
    result: dict | None


class ActiveTasks(BaseModel):
    count: int = 0
