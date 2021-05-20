"""empty message

Revision ID: c504a3d652e3
Revises: 14d412942f7a
Create Date: 2021-05-20 11:47:29.909482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c504a3d652e3'
down_revision = '14d412942f7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rental', 'customer_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('rental', 'video_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rental', 'video_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('rental', 'customer_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###