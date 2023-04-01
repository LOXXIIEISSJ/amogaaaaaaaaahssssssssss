"""Notification status

Revision ID: 99e9da74cae8
Revises: 45e42b78bc60
Create Date: 2023-02-23 17:42:26.137128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99e9da74cae8'
down_revision = '45e42b78bc60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('email', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_email_email'), ['email'])

    with op.batch_alter_table('notification', schema=None) as batch_op:
        batch_op.add_column(sa.Column('read', sa.Boolean(), nullable=False))

    with op.batch_alter_table('subtopic', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_subtopic_m_url'), ['m_url'])

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_user_email'), ['email'])
        batch_op.create_unique_constraint(batch_op.f('uq_user_username'), ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_username'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_user_email'), type_='unique')

    with op.batch_alter_table('subtopic', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_subtopic_m_url'), type_='unique')

    with op.batch_alter_table('notification', schema=None) as batch_op:
        batch_op.drop_column('read')

    with op.batch_alter_table('email', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_email_email'), type_='unique')

    # ### end Alembic commands ###
