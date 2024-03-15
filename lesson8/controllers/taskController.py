from http.client import HTTPException
from fastapi import FastAPI, Depends, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum, IntEnum
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, constr, ValidationError, validator, field_validator

task_router = APIRouter()

class STATUS(str, Enum):
    open = 'open'
    close = 'close'


class Task(BaseModel):
    name: constr(pattern=r"^[a-zA-Z0-9_]+$")
    description: str
    taskId: int
    status: STATUS


tasks = {}

def checkName(task: Task):
    if len(task.name) > 1:
        return task

@task_router.get("/")
async def get_tasks():
        return tasks


@task_router.post("/")
async def add_task(isCurrect: Task = Depends(checkName)):
    if isCurrect:
        try:
            tasks[isCurrect.taskId] = isCurrect
        except ValidationError:
            raise HTTPException(status_code=400, detail="oops... an error occurred")
        return f"Hello {isCurrect.name}"


@task_router.put("/{id}/", response_model=Task)
async def edit_task(taskid: int, task: Task):
    update_item_encoded = jsonable_encoder(task)
    tasks[taskid] = update_item_encoded
    return update_item_encoded


@task_router.delete("/{id}/")
async def delete_task(taskid: int):
    del tasks[taskid]
    return {"message": "Item deleted"}
