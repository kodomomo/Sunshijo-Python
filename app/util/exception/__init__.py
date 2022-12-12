import traceback

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


def initialize_exception_handler(app: FastAPI):
    @app.exception_handler(Exception)
    async def catch(req: Request, exc: Exception):
        if isinstance(exc, HTTPException) or issubclass(exc.__class__, HTTPException):
            raise exc

        return JSONResponse(
            status_code=500,
            content=jsonable_encoder(
                {
                    'exception': exc.__class__.__name__,
                    'detail': exc.args[0],
                    'traceback': traceback.format_exception(
                        etype=type(exc), value=exc, tb=exc.__traceback__
                    )
                }
            )
        )
