from typing import Iterable

from fastapi import FastAPI, APIRouter

from src.presentation.api.controllers.test import routers as test_routers


def _include_routers(app: FastAPI, routers: Iterable[APIRouter]):
    for router in routers:
        app.include_router(router)


def setup_routers(app: FastAPI):
    _include_routers(app, test_routers)
