from typing import Optional
from pydantic import BaseModel

# ! ВСЕ МОДЕЛИ И ЗАПРОСЫ см. В localhost:8000/docs !

class UserCreate(BaseModel):
    """ Модель данных для создания пользователя """
    tg_id: int
    user_university: str
    user_group: str
    user_first_name: str
    user_second_name: str
    user_last_name: str
    user_location: str

class UserUpdate(BaseModel):
    """ Модель данных для обновления пользователя """
    user_university: str
    user_group: str
    user_first_name: str
    user_second_name: str
    user_last_name: str
    user_location: str