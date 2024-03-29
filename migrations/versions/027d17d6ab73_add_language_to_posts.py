"""add language to posts

Revision ID: 027d17d6ab73
Revises: d48733acfab4
Create Date: 2019-08-01 04:27:24.057097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '027d17d6ab73'
down_revision = 'd48733acfab4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
