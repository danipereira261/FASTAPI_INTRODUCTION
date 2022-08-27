from unicodedata import name
from fastapi import APIRouter, HTTPException
from schemas import StandardOutput, UserCreateInput, ErrorOutput
from services import UserService

user_router = APIRouter(prefix="/user")
assets_router = APIRouter(prefix="/assets")


@user_router.post("/create",description="My description" ,response_model=StandardOutput, responses={400: {"model": ErrorOutput}})
async def user_create(user_input: UserCreateInput):
    try:
        await UserService.create_user(name=user_input.name)
        return StandardOutput(message="Ok")
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.delete("/delete/{user_id}", response_model=StandardOutput, responses={400: {"model": ErrorOutput}})
async def user_create(user_id: int):
    try:
        await UserService.delete_user(user_id)
        return StandardOutput(message="Ok")
    except Exception as error:
        raise HTTPException(400, detail=str(error))
