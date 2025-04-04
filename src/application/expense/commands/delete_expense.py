from didiator import Command, CommandHandler

from src.application.common.dto import DTO
from src.application.common.interfaces.uow import UnitOfWork
from src.application.expense.dto import ExpenseDTO
from src.application.expense.interfaces import ExpenseRepo


class DeleteExpense(DTO, Command[ExpenseDTO]):
    id: int


class DeleteExpenseHandler(CommandHandler[DeleteExpense, ExpenseDTO]):
    def __init__(self, repo: ExpenseRepo, uow: UnitOfWork):
        self.repo = repo
        self.uow = uow

    async def __call__(self, command: DeleteExpense) -> ExpenseDTO:
        expense = await self.repo.delete_one(id=command.id)
        await self.uow.commit()

        return expense
