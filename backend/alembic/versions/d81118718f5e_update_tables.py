"""update tables

Revision ID: d81118718f5e
Revises: 5e49a8a1938b
Create Date: 2024-04-10 15:33:49.681030

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd81118718f5e'
down_revision: Union[str, None] = '5e49a8a1938b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
