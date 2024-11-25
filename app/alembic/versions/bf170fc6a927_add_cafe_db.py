"""add Cafe DB

Revision ID: bf170fc6a927
Revises: 18d5565fe53e
Create Date: 2024-11-25 16:49:04.534553

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bf170fc6a927'
down_revision: Union[str, None] = '18d5565fe53e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cafe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=255), nullable=False),
    sa.Column('fish', sa.String(length=255), nullable=False),
    sa.Column('weight', sa.String(length=50), nullable=False),
    sa.Column('count', sa.Integer(), nullable=False),
    sa.Column('price', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cafe')
    # ### end Alembic commands ###