from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def initialize_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["localhost:3000", "http://localhost:3000/main", "http://localhost:3000", "*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
