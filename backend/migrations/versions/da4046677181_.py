"""empty message

Revision ID: da4046677181
Revises: 3755574a28ab
Create Date: 2020-11-10 00:39:22.321660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da4046677181'
down_revision = '3755574a28ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('levels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('difficulty', sa.String(), nullable=True),
    sa.Column('path', sa.Integer(), nullable=True),
    sa.Column('following_level', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['following_level'], ['levels.id'], ),
    sa.ForeignKeyConstraint(['path'], ['paths.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('levels')
    # ### end Alembic commands ###
