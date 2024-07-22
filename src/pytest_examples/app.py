from os import getenv
from fastapi import FastAPI
from dotenv import load_dotenv
from .controller import *
from fastapi.middleware.cors import CORSMiddleware
load_dotenv()

def app() -> FastAPI:

    app = FastAPI(
        redoc_url=None,
        title="Pytest",
        description="Pytest example",
        version=getenv("VERSION"),
        openapi_url='/openapi.json',
        docs_url="/swagger",
        root_path="/"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(main)
    app.include_router(security)

    return app

client = app()
