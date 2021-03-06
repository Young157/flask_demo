"""'init'

Revision ID: a0df0a7287b0
Revises: 
Create Date: 2020-09-17 21:28:02.567663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0df0a7287b0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=50), nullable=False),
    sa.Column('user_name', sa.String(length=50), nullable=False),
    sa.Column('user_password', sa.String(length=50), nullable=False),
    sa.Column('head_img', sa.String(length=200), nullable=True),
    sa.Column('short_description', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
