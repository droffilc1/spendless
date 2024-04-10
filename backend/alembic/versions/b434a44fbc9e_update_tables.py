"""Update tables

Revision ID: b434a44fbc9e
Revises: 5e5fd4ae52bd
Create Date: 2024-04-10 15:57:32.517136

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b434a44fbc9e'
down_revision: Union[str, None] = '5e5fd4ae52bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
