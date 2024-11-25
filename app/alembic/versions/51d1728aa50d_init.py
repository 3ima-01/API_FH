"""init

Revision ID: 51d1728aa50d
Revises: 
Create Date: 2024-11-20 17:58:54.645358

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '51d1728aa50d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('permissions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('unverified_users',
    sa.Column('user_id', sa.CHAR(length=36), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('verify_code', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('verify_code')
    )
    op.create_table('role_permissions',
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('permission_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['permission_id'], ['permissions.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('role_id', 'permission_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.CHAR(length=36), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('is_blocked', sa.Boolean(), server_default=sa.text('False'), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('points',
    sa.Column('uuid', sa.CHAR(length=36), nullable=False),
    sa.Column('user_id', sa.CHAR(length=36), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('fish', sa.String(length=255), nullable=False),
    sa.Column('location', sa.String(length=255), nullable=False),
    sa.Column('coords', sa.String(length=255), nullable=False),
    sa.Column('images', sa.JSON(), nullable=False),
    sa.Column('status', sa.Enum('PUBLISHED', 'DELETED', 'UNDER_MODERATION', 'DRAFT', 'SCHEDULED', name='statusenum'), server_default=sa.text("'DRAFT'"), nullable=False),
    sa.Column('create_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('update_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('profiles',
    sa.Column('uuid', sa.CHAR(length=36), nullable=False),
    sa.Column('user_uuid', sa.CHAR(length=36), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('avatar', sa.String(length=255), nullable=False),
    sa.Column('bio', sa.String(length=255), nullable=False),
    sa.Column('lvl', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_uuid'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles')
    op.drop_table('points')
    op.drop_table('users')
    op.drop_table('role_permissions')
    op.drop_table('unverified_users')
    op.drop_table('roles')
    op.drop_table('permissions')
    # ### end Alembic commands ###