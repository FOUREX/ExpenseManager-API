from fastapi import APIRouter

from src.presentation.api.providers.dependency import MediatorDep
from src.application.test.commands.create_test import CreateTest


test_router = APIRouter(prefix="/test", tags=["Tests"])
routers = (test_router, )


@test_router.post("")
async def post_test(
        mediator: MediatorDep,
        command: CreateTest
):
    return await mediator.send(command)
