"""Change password fieldname

Revision ID: bdcba65f3c5a
Revises: 522ef57098ad
Create Date: 2022-11-20 15:36:36.685618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdcba65f3c5a'
down_revision = '522ef57098ad'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(), nullable=True))
    op.drop_column('users', 'hashedPassword')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hashedPassword', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('users', 'password')
    # ### end Alembic commands ###
