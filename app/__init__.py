from fastapi import FastAPI

from app.core.schedule import include_schedule_router


def create_app():
    app = FastAPI()

    include_schedule_router(app)

    return app
