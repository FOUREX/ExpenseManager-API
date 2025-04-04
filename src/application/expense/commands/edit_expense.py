from decimal import Decimal

from didiator import Command, CommandHandler

from src.application.common.dto import DTO
from src.application.common.interfaces.uow import UnitOfWork
from src.application.expense.dto import ExpenseDTO, EditExpenseDTO, EditExpenseRequest
from src.application.expense.interfaces import ExpenseRepo
from src.infrastructure.currency_client import CurrencyClient


class EditExpense(DTO, Command[ExpenseDTO]):
    id: int
    data: EditExpenseRequest


class EditExpenseHandler(CommandHandler[EditExpense, ExpenseDTO]):
    def __init__(self, repo: ExpenseRepo, uow: UnitOfWork, currency_client: CurrencyClient):
        self.repo = repo
        self.uow = uow
        self.currency_client = currency_client

    async def __call__(self, command: EditExpense) -> ExpenseDTO:
        currency = await self.currency_client.get_usd_to_uah()

        edit_expense = EditExpenseDTO(
            **command.data.model_dump(),
            amount_usd=(command.data.amount_uah / Decimal(currency)).quantize(Decimal("0.01"))
        )

        expense = await self.repo.update_one(id=command.id, expense=edit_expense)
        await self.uow.commit()

        return expense
