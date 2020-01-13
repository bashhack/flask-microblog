"""user token creation

Revision ID: 97e78728ea8c
Revises: d38487c91938
Create Date: 2020-01-12 19:51:48.709720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97e78728ea8c'
down_revision = 'd38487c91938'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('token', sa.String(length=32), nullable=True))
    op.add_column('user', sa.Column('token_expiration', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_user_token'), 'user', ['token'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_token'), table_name='user')
    op.drop_column('user', 'token_expiration')
    op.drop_column('user', 'token')
    # ### end Alembic commands ###
