from typing import List
from asyncpg import Record

from models import user_models
from database import db


async def create_user(user: user_models.UserCreate) -> None:
    """ Функция добавления пользователя в базу """
    await db.connection.execute(
        """
        INSERT INTO users (
            tg_id,
            user_university,
            user_group,
            user_first_name,
            user_second_name,
            user_last_name,
            user_location)
        VALUES ($1, $2, $3, $4, $5, $6, $7)
        """,
        user.tg_id,
        user.user_university,
        user.user_group,
        user.user_first_name,
        user.user_second_name,
        user.user_last_name,
        user.user_location
    )

async def update_user(tg_id: int, user: user_models.UserUpdate) -> None:
    """ Функция обновления данных о пользователе """
    await db.connection.execute(
        """
        UPDATE users
        SET user_university=$1,
            user_group=$2,
            user_first_name=$3,
            user_second_name=$4,
            user_last_name=$5,
            user_location=$6
        WHERE tg_id=$7
        """,
        user.user_university,
        user.user_group,
        user.user_first_name,
        user.user_second_name,
        user.user_last_name,
        user.user_location,
        tg_id
    )

async def fetch_all_users() -> List[Record]:
    """ Функция получения всех пользователей """
    return await db.connection.fetch(
        """SELECT * FROM users"""
    ) 


async def fetch_user_by_tg_id(tg_id: int) -> Record:
    """ Функция получения пользователя по tg_id """
    return await db.connection.fetchrow(
        """SELECT * FROM users WHERE tg_id=$1""",
        tg_id
    )
