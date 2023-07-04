"""add_messages3

Revision ID: 532fd72e9937
Revises: bef760ff3969
Create Date: 2023-07-03 15:44:24.195154

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '532fd72e9937'
down_revision = 'bef760ff3969'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('text', sa.String(), nullable=False))
    op.add_column('message', sa.Column('sent_at', sa.DateTime(), nullable=True))
    op.alter_column('message', 'sender_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_index(op.f('ix_message_id'), 'message', ['id'], unique=False)
    op.drop_constraint('message_recipient_id_fkey', 'message', type_='foreignkey')
    op.drop_column('message', 'content')
    op.drop_column('message', 'recipient_id')
    op.drop_column('message', 'created_at')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('message', sa.Column('recipient_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('message', sa.Column('content', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.create_foreign_key('message_recipient_id_fkey', 'message', 'user', ['recipient_id'], ['id'])
    op.drop_index(op.f('ix_message_id'), table_name='message')
    op.alter_column('message', 'sender_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('message', 'sent_at')
    op.drop_column('message', 'text')
    # ### end Alembic commands ###