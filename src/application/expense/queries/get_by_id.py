from didiator import Query, QueryHandler

from src.application.common.dto import DTO
from src.application.expense.dto import ExpenseDTO
from src.application.expense.interfaces import ExpenseReader


class GetByID(DTO, Query[ExpenseDTO | None]):
    id: int


class GetByIDHandler(QueryHandler[GetByID, ExpenseDTO | None]):
    def __init__(self, reader: ExpenseReader):
        self.reader = reader

    async def __call__(self, query: GetByID) -> ExpenseDTO | None:
        return await self.reader.select_one(id=query.id)
