"""empty message

Revision ID: 20d2c751e348
Revises: 7803acfacc15
Create Date: 2016-10-10 19:25:41.743398

"""

# revision identifiers, used by Alembic.
revision = '20d2c751e348'
down_revision = '7803acfacc15'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    ### end Alembic commands ###
