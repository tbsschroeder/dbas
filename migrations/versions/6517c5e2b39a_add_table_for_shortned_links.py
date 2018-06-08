"""Add

Revision ID: 6517c5e2b39a
Revises: cfd456c47b69
Create Date: 2018-06-07 06:52:42.668697

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op

# revision identifiers, used by Alembic.
revision = '6517c5e2b39a'
down_revision = 'cfd456c47b69'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('short_links',
                    sa.Column('uid', sa.Integer(), nullable=False),
                    sa.Column('service', sa.Text(), nullable=False),
                    sa.Column('long_url', sa.Text(), nullable=False),
                    sa.Column('short_url', sa.Text(), nullable=False),
                    sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
                    sa.PrimaryKeyConstraint('uid')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('short_links')
    # ### end Alembic commands ###