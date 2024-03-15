import uvicorn as uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, constr, ValidationError, validator, field_validator
from enum import Enum, IntEnum

app = FastAPI()


class STATUS(str, Enum):
    open = 'open'
    close = 'close'


class Task(BaseModel):
    name: constr(pattern=r"^[a-zA-Z0-9_]+$")
    description: str
    taskId: int
    status: STATUS

    # @field_validator('id')
    # def check_id(cls, id):
    #     if id < 1:
    #         raise ValueError('error')
    #     return id
    #
    # @field_validator('description')
    # def check_description(cls, description):
    #     if len(description) > 100:
    #         raise ValueError('error')
    #     return description


tasks = {}


@app.get("/")
async def get_tasks():
    return tasks


@app.post("/")
async def add_task(task: Task):
    try:
        tasks[task.taskId] = task
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return f"Hello {task.name}"


@app.put("/{id}/", response_model=Task)
async def edit_task(taskid: int, task: Task):
    update_item_encoded = jsonable_encoder(task)
    tasks[taskid] = update_item_encoded
    return update_item_encoded


@app.delete("/{id}/")
async def delete_task(taskid: int):
    del tasks[taskid]
    return {"message": "Item deleted"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8080)
