from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def initialize_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "https://boisterous-paprenjak-b40c12.netlify.app/",
            "*"
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
