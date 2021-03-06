"""Add Guild table to facilitate public guild views.

Revision ID: 4af4c837801f
Revises: a8a516f57e97
Create Date: 2016-08-26 22:37:26.306500

"""

# revision identifiers, used by Alembic.
revision = '4af4c837801f'
down_revision = 'a8a516f57e97'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('guild',
    sa.Column('id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('icon', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('public', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('guild')
    ### end Alembic commands ###
