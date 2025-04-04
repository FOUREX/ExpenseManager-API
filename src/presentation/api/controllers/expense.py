from typing import Annotated, Sequence
from datetime import datetime

from fastapi import APIRouter, Path, Query, status

from src.application.expense.queries.get_between import GetBetween
from src.presentation.api.providers.dependency import MediatorDep
from src.application.expense.dto import ExpenseDTO, EditExpenseRequest
from src.application.expense.queries.get_by_id import GetByID
from src.application.expense.commands.create_expense import CreateExpense
from src.application.expense.commands.edit_expense import EditExpense
from src.application.expense.commands.delete_expense import DeleteExpense


expense_router = APIRouter(prefix="/expense", tags=["Expenses"])
expenses_router = APIRouter(prefix="/expenses", tags=["Expenses"])
routers = (expense_router, expenses_router)


@expense_router.get(
    "/{id}",
    description="Повертає статтю за її ID, або null якщо її не існує"
)
async def get_expense(
        mediator: MediatorDep,
        id: Annotated[int, Path()]
) -> ExpenseDTO | None:
    return await mediator.query(GetByID(id=id))


@expense_router.post(
    "",
    description="Створює статтю та повертає її з всіма даними",
    status_code=status.HTTP_201_CREATED
)
async def post_expense(
        mediator: MediatorDep,
        command: CreateExpense
) -> ExpenseDTO:
    return await mediator.send(command)


@expense_router.patch(
    "/{id}",
    description="Редагує статтю за її ID та повертає її (якщо існує) з всіма даними. Не обов'язково передавати всі поля"
)
async def patch_expense(
        mediator: MediatorDep,
        id: Annotated[int, Path()],
        expense: EditExpenseRequest
) -> ExpenseDTO | None:
    return await mediator.send(EditExpense(id=id, data=expense))


@expense_router.delete(
    "/{id}",
    description="Видаляє статтю за її ID та повертає її з всіма даними"
)
async def delete_expense(
        mediator: MediatorDep,
        id: Annotated[int, Path()]
) -> ExpenseDTO | None:
    return await mediator.send(DeleteExpense(id=id))


@expenses_router.get(
    "",
    description="Повертає всі статті які знаходяться в заданому діапазоні дат (включно), або порожній список"
)
async def get_expenses(
        mediator: MediatorDep,
        start_date: Annotated[datetime | None, Query()] = None,
        end_date: Annotated[datetime | None, Query()] = None
) -> Sequence[ExpenseDTO]:
    return await mediator.query(GetBetween(start_date=start_date, end_date=end_date))
