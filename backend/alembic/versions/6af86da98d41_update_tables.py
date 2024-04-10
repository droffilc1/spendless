"""update tables

Revision ID: 6af86da98d41
Revises: d81118718f5e
Create Date: 2024-04-10 15:36:00.496618

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6af86da98d41'
down_revision: Union[str, None] = 'd81118718f5e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
