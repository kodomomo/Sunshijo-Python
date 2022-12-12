from fastapi import FastAPI


def include_record_router(app: FastAPI):
    from app.core.record.view import record_router

    app.include_router(record_router)
