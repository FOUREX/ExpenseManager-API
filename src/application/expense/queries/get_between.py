from typing import Sequence
from datetime import datetime

from didiator import Query, QueryHandler

from src.application.common.dto import DTO
from src.application.expense.dto import ExpenseDTO
from src.application.expense.interfaces import ExpenseReader


class GetBetween(DTO, Query[Sequence[ExpenseDTO]]):
    start_date: datetime | None = None
    end_date: datetime | None = None


class GetBetweenHandler(QueryHandler[GetBetween, Sequence[ExpenseDTO]]):
    def __init__(self, reader: ExpenseReader):
        self.reader = reader

    async def __call__(self, query: GetBetween) -> Sequence[ExpenseDTO]:
        return await self.reader.select_between(start_date=query.start_date, end_date=query.end_date)
