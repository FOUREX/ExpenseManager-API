from datetime import datetime

from sqlalchemy import String, DECIMAL, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.db.models.base import Base


class ExpenseORM(Base):
    __tablename__ = "Expense"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(length=128))
    amount_uah: Mapped[float] = mapped_column(DECIMAL(15, 2))
    amount_usd: Mapped[float] = mapped_column(DECIMAL(15, 2))
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
