from http.client import HTTPException
from fastapi import FastAPI, Depends, APIRouter
from enum import Enum, IntEnum
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, constr, ValidationError, validator, field_validator

user_router = APIRouter()


class User(BaseModel):
    name: str
    id: int

users = {}

def checkId(user: User):
    if user.id > 0:
        return user

@user_router.get("/")
async def get_tasks():
    return users

@user_router.post("/")
async def add_user(isCurrect: User = Depends(checkId)):
    try:
        users[isCurrect.id] = isCurrect
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return f"Hello {isCurrect.name}"


@user_router.put("/{id}/", response_model=User)
async def edit_user(id: int, user: User):
    update_item_encoded = jsonable_encoder(user)
    users[id] = update_item_encoded
    return update_item_encoded


@user_router.delete("/{id}/")
async def delete_user(id: int):
    del users[id]
    return {"message": "Item deleted"}