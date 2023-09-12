"""empty message

Revision ID: c00b20828b61
Revises: 
Create Date: 2023-09-12 11:09:00.415763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c00b20828b61'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('engineers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('specialty', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('certificates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('expiration_year', sa.Integer(), nullable=True),
    sa.Column('engineer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['engineer_id'], ['engineers.id'], name=op.f('fk_certificates_engineer_id_engineers')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('certificates')
    op.drop_table('engineers')
    # ### end Alembic commands ###