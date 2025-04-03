from typing import Protocol, Type

from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.db.models.base import Base
from src.infrastructure.db.mappers.base import BaseMapper


class BaseRepo[Model: Base, Mapper: BaseMapper](Protocol):
    model: Type[Model]
    mapper: Type[Mapper]

    def __init__(self, session: AsyncSession):
        self.session = session
