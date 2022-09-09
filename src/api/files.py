import os

from fastapi import APIRouter, Depends, HTTPException

from src import config

from src.services import files

router = APIRouter(prefix="/file", tags=["files"])


@router.get("/sum-every/{delta}/columns")
async def sum_columns(
    delta: int,
    filename: str,
    settings: config.Settings = Depends(config.get_settings),
):
    filepath = os.path.join(settings.STORAGE_PATH, filename)
    if not filename.endswith(".csv") or not os.path.isfile(filepath):
        raise HTTPException(
            status_code=400, detail=f"Filename is not valid ({filepath=})"
        )
    task = files.process.delay(filepath, delta)
    return {"task_id": task.id}
