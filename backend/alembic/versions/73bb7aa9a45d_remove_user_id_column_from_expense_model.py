"""Remove user_id column from Expense model

Revision ID: 73bb7aa9a45d
Revises: b434a44fbc9e
Create Date: 2024-04-18 15:19:15.222433

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '73bb7aa9a45d'
down_revision: Union[str, None] = 'b434a44fbc9e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('expenses_ibfk_2', 'expenses', type_='foreignkey')
    op.drop_column('expenses', 'user_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('expenses', sa.Column('user_id', mysql.VARCHAR(length=60), nullable=False))
    op.create_foreign_key('expenses_ibfk_2', 'expenses', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###