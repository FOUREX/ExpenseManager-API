from datetime import datetime

from pydantic import Field, condecimal

from src.application.common.dto import DTO


class ExpenseDTO(DTO):
    id: int
    name: str = Field(max_length=128)
    amount_uah: condecimal(gt=0, max_digits=15, decimal_places=2)
    amount_usd: condecimal(gt=0, max_digits=15, decimal_places=2)
    created_at: datetime


class CreateExpenseRequest(DTO):
    name: str = Field(max_length=128)
    amount_uah: condecimal(gt=0, max_digits=15, decimal_places=2)
    created_at: datetime


class CreateExpenseDTO(CreateExpenseRequest):
    amount_usd: condecimal(gt=0, max_digits=15, decimal_places=2)


class EditExpenseRequest(DTO):
    name: str | None = Field(default=None, max_length=128)
    amount_uah: condecimal(gt=0, max_digits=15, decimal_places=2) | None = Field(default=None)
    created_at: datetime | None = Field(default=None)


class EditExpenseDTO(EditExpenseRequest):
    amount_usd: condecimal(gt=0, max_digits=15, decimal_places=2) | None = Field(default=None)
