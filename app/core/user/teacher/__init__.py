from fastapi import FastAPI


def include_teacher_router(app: FastAPI):
    from app.core.user.teacher.view import teacher_router

    app.include_router(teacher_router)
