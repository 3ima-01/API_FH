"""add rods and coils DB

Revision ID: 18d5565fe53e
Revises: 96034ad30eee
Create Date: 2024-11-25 15:02:36.666362

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '18d5565fe53e'
down_revision: Union[str, None] = '96034ad30eee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coils',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('mex', sa.Double(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('mex', sa.Double(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rods')
    op.drop_table('coils')
    # ### end Alembic commands ###