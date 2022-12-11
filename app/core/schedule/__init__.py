from fastapi import FastAPI


def include_schedule_router(app: FastAPI):
    from app.core.schedule.view import schedule_router

    app.include_router(schedule_router)
