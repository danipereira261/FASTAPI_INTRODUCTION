from typing import List
from fastapi import APIRouter, HTTPException
from schemas import StandardOutput, UserCreateInput, ErrorOutput, UserFavoriteAddInput, UserListOutput
from services import UserService, FavoriteService

user_router = APIRouter(prefix="/user")
assets_router = APIRouter(prefix="/assets")


@user_router.post("/create", description="My description", response_model=StandardOutput, responses={400: {"model": ErrorOutput}})
async def user_create(user_input: UserCreateInput):
    try:
        await UserService.create_user(name=user_input.name)
        return StandardOutput(message="Ok")
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.delete("/delete/{user_id}", response_model=StandardOutput, responses={400: {"model": ErrorOutput}})
async def user_delete(user_id: int):
    try:
        await UserService.delete_user(user_id)
        return StandardOutput(message="Ok")
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.post("/favorite/add", response_model=StandardOutput, responses={400: {"model": ErrorOutput}})
async def user_favorite_add(favorite_add: UserFavoriteAddInput):
    try:
        await FavoriteService.add_favorite(user_id=favorite_add.user_id, symbol=favorite_add.symbol)
        return StandardOutput(message="Ok")
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.delete("favorite/remove/{user_id}", response_model=StandardOutput, responses={400: {"model": ErrorOutput}})
async def user_delete(user_id: int, symbol: str):
    try:
        await FavoriteService.remove_favorite(user_id=user_id, symbol=symbol)
        return StandardOutput(message="Ok")
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.get("/list", response_model=List[UserListOutput], responses={400:{"model": ErrorOutput}})
async def user_list():
    try:
        return await UserService.list_user()
    except Exception as error:
        raise HTTPException(400, detail=str(error))
