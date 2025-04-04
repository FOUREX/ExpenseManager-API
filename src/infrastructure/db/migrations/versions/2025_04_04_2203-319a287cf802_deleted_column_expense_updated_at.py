"""Deleted column Expense.updated_at

Revision ID: 319a287cf802
Revises: 13be29089e1b
Create Date: 2025-04-04 22:03:00.884077

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "319a287cf802"
down_revision: Union[str, None] = "13be29089e1b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_column("Expense", "updated_at")


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        "Expense",
        sa.Column(
            "updated_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=False
        ),
    )
