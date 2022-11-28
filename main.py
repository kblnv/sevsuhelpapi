from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import config
from database import db
from routers import user_routes

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(user_routes.users_router, prefix="/api/v1")


@app.on_event("startup")
async def startup():
    await db.init(
        config.DB_USER,
        config.DB_PASSWORD,
        config.DB_HOST,
        config.DB_NAME
    )


@app.on_event("shutdown")
async def shutdown():
    await db.close()
