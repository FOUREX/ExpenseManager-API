"""Fixed Expense.updated_at

Revision ID: 13be29089e1b
Revises: ef64fab91c9d
Create Date: 2025-04-04 00:29:03.989989

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "13be29089e1b"
down_revision: Union[str, None] = "ef64fab91c9d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
        UPDATE public."Expense"
        SET updated_at = created_at
        WHERE updated_at IS NULL;
    """)

    op.alter_column(
        "Expense", "updated_at", existing_type=postgresql.TIMESTAMP(), nullable=False
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "Expense", "updated_at", existing_type=postgresql.TIMESTAMP(), nullable=True
    )
