"""Increase password column size

Revision ID: 5e49a8a1938b
Revises: 
Create Date: 2024-04-01 22:29:11.242674

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '5e49a8a1938b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('categories', 'id',
               existing_type=mysql.VARCHAR(length=36),
               type_=sa.String(length=60),
               existing_nullable=False)
    op.alter_column('expenses', 'category_id',
               existing_type=mysql.VARCHAR(length=36),
               type_=sa.String(length=60),
               existing_nullable=True)
    op.alter_column('expenses', 'user_id',
               existing_type=mysql.VARCHAR(length=36),
               type_=sa.String(length=60),
               existing_nullable=False)
    op.alter_column('expenses', 'id',
               existing_type=mysql.VARCHAR(length=36),
               type_=sa.String(length=60),
               existing_nullable=False)
    op.alter_column('users', 'password',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=255),
               existing_nullable=False)
    op.alter_column('users', 'id',
               existing_type=mysql.VARCHAR(length=36),
               type_=sa.String(length=60),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'id',
               existing_type=sa.String(length=60),
               type_=mysql.VARCHAR(length=36),
               existing_nullable=False)
    op.alter_column('users', 'password',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)
    op.alter_column('expenses', 'id',
               existing_type=sa.String(length=60),
               type_=mysql.VARCHAR(length=36),
               existing_nullable=False)
    op.alter_column('expenses', 'user_id',
               existing_type=sa.String(length=60),
               type_=mysql.VARCHAR(length=36),
               existing_nullable=False)
    op.alter_column('expenses', 'category_id',
               existing_type=sa.String(length=60),
               type_=mysql.VARCHAR(length=36),
               existing_nullable=True)
    op.alter_column('categories', 'id',
               existing_type=sa.String(length=60),
               type_=mysql.VARCHAR(length=36),
               existing_nullable=False)
    # ### end Alembic commands ###
