from typing import Sequence
from datetime import datetime

from sqlalchemy import select, insert, update, delete

from src.infrastructure.db.repositories.base import BaseRepo
from src.infrastructure.db.models.expense import ExpenseORM
from src.infrastructure.db.mappers.expense import ExpenseMapper
from src.application.expense.interfaces import ExpenseRepo, ExpenseReader
from src.application.expense.dto import ExpenseDTO, CreateExpenseDTO, EditExpenseDTO


class ExpenseRepoImpl(BaseRepo[ExpenseORM, ExpenseMapper], ExpenseRepo):
    model = ExpenseORM
    mapper = ExpenseMapper

    async def insert_one(self, expense: CreateExpenseDTO) -> ExpenseDTO:
        stmt = (
            insert(self.model)
            .values(self.mapper.to_dict(expense))
            .returning(self.model)
        )

        result = await self.session.scalar(stmt)

        return self.mapper.from_orm(result)

    async def update_one(self, id: int, expense: EditExpenseDTO) -> ExpenseDTO:
        stmt = (
            update(self.model)
            .values(self.mapper.to_dict(expense))
            .where(self.model.id == id)
            .returning(self.model)
        )

        result = await self.session.scalar(stmt)

        return self.mapper.from_orm(result)

    async def delete_one(self, id: int) -> ExpenseDTO | None:
        stmt = (
            delete(self.model)
            .where(self.model.id == id)
            .returning(self.model)
        )

        result = await self.session.scalar(stmt)

        return None if result is None else self.mapper.from_orm(result)


class ExpenseReaderImpl(BaseRepo[ExpenseORM, ExpenseMapper], ExpenseReader):
    model = ExpenseORM
    mapper = ExpenseMapper

    async def select_one(self, id: int) -> ExpenseDTO | None:
        query = (
            select(self.model)
            .where(self.model.id == id)
        )

        result = await self.session.scalar(query)

        return None if result is None else self.mapper.from_orm(result)

    async def select_between(
            self,
            start_date: datetime | None = None,
            end_date: datetime | None = None
    ) -> Sequence[ExpenseDTO]:
        query = (
            select(self.model)
        )

        if start_date is not None:
            query = query.where(self.model.created_at >= start_date)

        if end_date is not None:
            query = query.where(self.model.created_at <= end_date)

        results = await self.session.scalars(query)

        return [self.mapper.from_orm(result) for result in results]
