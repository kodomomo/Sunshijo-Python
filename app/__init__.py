from fastapi import FastAPI

from app.common.security.auth import initialize_token_security
from app.core.record import include_record_router
from app.core.schedule import include_schedule_router
from app.core.user.teacher import include_teacher_router

from app.common.exception import initialize_exception_handler

from app.infrastructure.database.mysql.model import create_all_table

from app.util.macro import run_macro


def create_app():
    app = FastAPI()

#    run_macro()

    create_all_table()

    include_schedule_router(app)
    include_teacher_router(app)
    include_record_router(app)

    initialize_exception_handler(app)
    initialize_token_security(app)

    return app
