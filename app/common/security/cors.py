from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def initialize_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "https://helpful-hummingbird-429b7b.netlify.app/",
            "*"
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
