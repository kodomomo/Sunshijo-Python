from fastapi import FastAPI

from app.core.schedule import include_schedule_router
from app.util.exception import initialize_exception_handler

from app.util.dao.mysql import create_all_table


def create_app():
    app = FastAPI()

    include_schedule_router(app)

    initialize_exception_handler(app)

    create_all_table()

    return app
