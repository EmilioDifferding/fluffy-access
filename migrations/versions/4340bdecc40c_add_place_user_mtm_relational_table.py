"""add place_user mtm relational table

Revision ID: 4340bdecc40c
Revises: 3b2eefed05bd
Create Date: 2021-11-25 17:49:10.715243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4340bdecc40c'
down_revision = '3b2eefed05bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('place_user',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('place_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['place_id'], ['places.id'], name=op.f('fk_place_user_place_id_places')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_place_user_user_id_users'))
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint('fk_users_place_id_places', type_='foreignkey')
        batch_op.drop_column('place_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('place_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_users_place_id_places', 'places', ['place_id'], ['id'])

    op.drop_table('place_user')
    # ### end Alembic commands ###
