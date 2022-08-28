from select import select
from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy.future import select
from sqlalchemy import delete

from database.models import Favorite, User
from database.connection import async_session


class UserService:
    async def create_user(name: str):
        async with async_session() as session:
            session.add(User(name=name))
            await session.commit()

    async def delete_user(user_id: int):
        async with async_session() as session:
            await session.execute(delete(User).where(User.id == user_id))
            await session.commit()

    async def list_user():
            async with async_session() as session:
                result = await session.execute(select(User).where())
                return result.scalars().all()


class FavoriteService:
    async def add_favorite(user_id: int, symbol: str):
        async with async_session() as session:
            session.add(Favorite(user_id=user_id, symbol=symbol))
            await session.commit()

    async def remove_favorite(user_id: int, symbol: str):
        async with async_session() as session:
            await session.execute(delete(Favorite).where(Favorite.user_id == user_id, Favorite.symbol == symbol))
            await session.commit()
