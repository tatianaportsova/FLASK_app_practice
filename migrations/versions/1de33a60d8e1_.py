"""empty message

Revision ID: 1de33a60d8e1
Revises: 
Create Date: 2020-03-25 18:02:25.192088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1de33a60d8e1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('author_id', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('screen_name', sa.String(length=128), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('followers_count', sa.Integer(), nullable=True),
    sa.Column('latest_tweet_id', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tweet',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.Column('full_text', sa.String(length=500), nullable=True),
    sa.Column('embedding', sa.PickleType(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tweet')
    op.drop_table('user')
    op.drop_table('book')
    # ### end Alembic commands ###
