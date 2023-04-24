from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.controllers import base_controller


def get_application() -> FastAPI:
    application = FastAPI()

    origins = [
        "http://localhost",
    ]

    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(base_controller.controller, prefix="/api")

    return application


app = get_application()
