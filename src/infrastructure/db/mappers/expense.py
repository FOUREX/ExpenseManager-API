from src.infrastructure.db.mappers.base import BaseMapper
from src.infrastructure.db.models.expense import ExpenseORM
from src.application.expense.dto import ExpenseDTO


class ExpenseMapper(BaseMapper[ExpenseORM, ExpenseDTO]):
    model = ExpenseORM
    schema = ExpenseDTO
