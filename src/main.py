from fastapi import FastAPI

from .api import router

tags_metadata = [
    {
        "name": "files",
        "description": "Работа с файлами",
    },
    {
        "name": "tasks",
        "description": "Информация о задачах",
    },
]

app = FastAPI(
    title="CSV Processor",
    description="Обработка больших csv файлов",
    version="1.0.0",
    openapi_tags=tags_metadata,
)
app.include_router(router)
