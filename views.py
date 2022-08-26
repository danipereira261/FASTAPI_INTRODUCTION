from unicodedata import name
from fastapi import APIRouter
from schemas import UserCreateInput, StandardOutput
from services import UserService

user_router = APIRouter(prefix="/user")
assets_router = APIRouter(prefix="/assets")


@user_router.post("/create", response_model=StandardOutput)
async def user_create(user_input: UserCreateInput):
    try:
        await UserService.create_user(name=user_input.name)
        return StandardOutput(message="Ok")
    except:
        pass

