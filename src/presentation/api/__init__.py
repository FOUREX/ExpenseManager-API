from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.infrastructure.di import init_di_builder, setup_di_builder
from src.infrastructure.di.constants import DiScope
from src.infrastructure.mediator import init_mediator, setup_mediator
from src.presentation.api.providers import setup_providers
from src.presentation.api.controllers import setup_routers


@asynccontextmanager
async def init_app(app: FastAPI):
    di_builder = init_di_builder()
    setup_di_builder(di_builder)

    async with di_builder.enter_scope(DiScope.APP) as di_state:
        mediator = await di_builder.execute(init_mediator, DiScope.APP, state=di_state)
        setup_mediator(mediator)

        setup_providers(app, mediator, di_builder, di_state)
        setup_routers(app)

        yield


def init_api() -> FastAPI:
    app = FastAPI(
        title="Менеджер витрат",
        description="Created by <a href='https://t.me/Serhii_Zherevchuk' target='blank'>Serhii Zherevchuk</a> "
                    "for <a href='https://www.mustage.team' target='blank'>Mustage Team</a>",
        lifespan=init_app,
        version="0.0.2"
    )

    return app
