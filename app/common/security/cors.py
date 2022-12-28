from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def initialize_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "https://sunshijo-frontend.vercel.app/",
            "https://sunshijo-frontend.vercel.app/main",
            "*"
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
