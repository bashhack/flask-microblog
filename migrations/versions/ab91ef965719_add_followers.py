"""add followers

Revision ID: ab91ef965719
Revises: fa8a9de067d9
Create Date: 2020-01-05 14:30:29.292813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ab91ef965719"
down_revision = "fa8a9de067d9"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "followers",
        sa.Column("follower_id", sa.Integer(), nullable=True),
        sa.Column("followed_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["followed_id"], ["user.id"],),
        sa.ForeignKeyConstraint(["follower_id"], ["user.id"],),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("followers")
    # ### end Alembic commands ###
