from typing import Iterable

from fastapi import FastAPI, APIRouter

from src.presentation.api.controllers.expense import routers as expense_routers


def _include_routers(app: FastAPI, routers: Iterable[APIRouter]):
    for router in routers:
        app.include_router(router)


def setup_routers(app: FastAPI):
    _include_routers(app, expense_routers)
