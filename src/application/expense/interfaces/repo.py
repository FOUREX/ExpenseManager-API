from typing import Protocol

from src.application.expense.dto import ExpenseDTO, CreateExpenseDTO, EditExpenseDTO


class ExpenseRepo(Protocol):
    async def insert_one(self, expense: CreateExpenseDTO) -> ExpenseDTO:
        raise NotImplementedError

    async def update_one(self, id: int, expense: EditExpenseDTO) -> ExpenseDTO:
        raise NotImplementedError

    async def delete_one(self, id: int) -> ExpenseDTO | None:
        raise NotImplementedError
