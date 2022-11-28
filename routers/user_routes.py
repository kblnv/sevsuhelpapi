from fastapi import APIRouter, Body
from database import user_db
from models import user_models

users_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@users_router.post("/create")
async def create_user(user: user_models.UserCreate):
    """ Ручка для создания пользователя """
    await user_db.create_user(user)
    return {"tg_id": user.tg_id}


@users_router.put("/update")
async def update_user(tg_id: int, user: user_models.UserUpdate):
    """ Ручка для обновления данных о пользователе """
    await user_db.update_user(tg_id, user)
    return {"tg_id": tg_id}


@users_router.post("/add-sos")
async def add_sos_user(tg_id: int):
    """ Ручка для добавления пользователя в список тех, кто нажал на SOS """
    await user_db.add_user_to_sos(tg_id)
    return {"tg_id": tg_id}


@users_router.get("/get/{tg_id}")
async def get_user(tg_id: int):
    """ Ручка для получения пользователя """
    return await user_db.fetch_user_by_tg_id(tg_id)


@users_router.get("/get-all")
async def get_all_users():
    """ Ручка для получения всех пользователей """
    return await user_db.fetch_all_users()


@users_router.get("/get-all-sos")
async def get_sos_users():
    """ Ручка для получения всех пользователей, которые нажали SOS """
    return await user_db.fetch_sos_users()
