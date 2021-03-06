"""empty message

Revision ID: 35a4c25f12e5
Revises: 81e78fdad2ed
Create Date: 2018-07-29 20:41:44.100599

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '35a4c25f12e5'
down_revision = '81e78fdad2ed'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('is_stripe_linked', sa.Boolean(), nullable=True))
    op.add_column('events_version', sa.Column('is_stripe_linked', sa.Boolean(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events_version', 'is_stripe_linked')
    op.drop_column('events', 'is_stripe_linked')
    # ### end Alembic commands ###
