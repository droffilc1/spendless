"""update tables

Revision ID: d61f8a16ccd2
Revises: 6af86da98d41
Create Date: 2024-04-10 15:37:01.953202

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd61f8a16ccd2'
down_revision: Union[str, None] = '6af86da98d41'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
