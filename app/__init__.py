from fastapi import FastAPI

from app.teacher import teacher_router


def create_app():
    app = FastAPI()

    app.include_router(teacher_router, tags=['Teacher'])

    return app
