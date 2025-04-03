from typing import Protocol, Sequence
from datetime import datetime

from src.application.expense.dto import ExpenseDTO


class ExpenseReader(Protocol):
    async def select_one(self, id: int) -> ExpenseDTO | None:
        raise NotImplementedError

    async def select_between(
            self,
            start_date: datetime | None = None,
            end_date: datetime | None = None
    ) -> Sequence[ExpenseDTO]:
        raise NotImplementedError
