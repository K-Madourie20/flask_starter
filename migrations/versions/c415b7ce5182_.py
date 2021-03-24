"""empty message

Revision ID: c415b7ce5182
Revises: 
Create Date: 2021-03-23 22:14:26.513864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c415b7ce5182'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Title', sa.String(length=80), nullable=True),
    sa.Column('details', sa.String(length=80), nullable=True),
    sa.Column('rooms', sa.Integer(), nullable=True),
    sa.Column('bathroom', sa.Integer(), nullable=True),
    sa.Column('cost', sa.Integer(), nullable=True),
    sa.Column('located', sa.String(length=50), nullable=True),
    sa.Column('prop_type', sa.String(length=20), nullable=True),
    sa.Column('photo', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    # ### end Alembic commands ###