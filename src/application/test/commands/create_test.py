from didiator import Command, CommandHandler
from sqlalchemy.ext.asyncio import AsyncSession
from didiator.interface.utils.di_builder import DiBuilder

from src.application.common.dto import DTO
from src.application.common.interfaces.uow import UnitOfWork


class CreateTest(DTO, Command[None]):
    name: str


class CreateTestHandler(CommandHandler[CreateTest, None]):
    def __init__(self, session: AsyncSession, di_builder: DiBuilder, uow: UnitOfWork):
        print(session, di_builder, uow)

    async def __call__(self, command: CreateTest) -> None:
        print(command)

        return None
