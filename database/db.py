import asyncpg


async def init(
    db_user: str,
    db_password: str,
    db_host: str,
    db_name: str
):
    """ Функция подключения к базе данных и инициализации таблиц """
    global connection
    connection = await asyncpg.connect(f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}")

    await connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id               SERIAL,
            tg_id            BIGINT       UNIQUE, 
            user_university  VARCHAR(128) CHECK(user_university != ''),
            user_group       VARCHAR(24)  CHECK(user_group != ''),
            user_first_name  VARCHAR(32)  CHECK(user_first_name != ''),
            user_second_name VARCHAR(32)  CHECK(user_second_name != ''),
            user_last_name   VARCHAR(32)  CHECK(user_last_name != ''),
            user_location    VARCHAR(128) CHECK(user_location != ''),
    
            PRIMARY KEY (user_first_name, user_second_name, user_last_name)
        );

        CREATE TABLE IF NOT EXISTS sos_users (
            tg_id BIGINT,
            FOREIGN KEY (tg_id) REFERENCES users (tg_id) ON DELETE CASCADE
        );

    """)


async def close():
    await connection.close()
