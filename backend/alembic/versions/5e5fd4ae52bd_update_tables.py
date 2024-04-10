"""Update tables

Revision ID: 5e5fd4ae52bd
Revises: e0450bd4f880
Create Date: 2024-04-10 15:48:14.298094

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e5fd4ae52bd'
down_revision: Union[str, None] = 'e0450bd4f880'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
