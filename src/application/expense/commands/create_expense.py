from decimal import Decimal

from didiator import Command, CommandHandler

from src.application.common.interfaces.uow import UnitOfWork
from src.application.expense.dto import ExpenseDTO, CreateExpenseDTO, CreateExpenseRequest
from src.application.expense.interfaces import ExpenseRepo
from src.infrastructure.currency_client import CurrencyClient


class CreateExpense(CreateExpenseRequest, Command[ExpenseDTO]):
    ...


class CreateExpenseHandler(CommandHandler[CreateExpense, ExpenseDTO]):
    def __init__(self, repo: ExpenseRepo, uow: UnitOfWork, currency_client: CurrencyClient):
        self.repo = repo
        self.uow = uow
        self.currency_client = currency_client

    async def __call__(self, command: CreateExpense) -> ExpenseDTO:
        currency = await self.currency_client.get_usd_to_uah()

        create_expense = CreateExpenseDTO(
            **command.model_dump(),
            amount_usd=(command.amount_uah / Decimal(currency)).quantize(Decimal("0.01"))
        )

        expense = await self.repo.insert_one(expense=create_expense)
        await self.uow.commit()

        return expense
