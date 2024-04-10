"""Update tables

Revision ID: e0450bd4f880
Revises: d61f8a16ccd2
Create Date: 2024-04-10 15:38:39.266080

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0450bd4f880'
down_revision: Union[str, None] = 'd61f8a16ccd2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
