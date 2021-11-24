"""Initial migration

Revision ID: 9229b3872535
Revises: 
Create Date: 2021-11-24 23:12:01.442524

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9229b3872535'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('application_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_timestamp', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('last_modified_timestamp', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('date_of_birth', sa.Date(), nullable=True),
    sa.Column('role', sa.Enum('ADMIN', 'CLIENT', name='roles'), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_application_user_email'), 'application_user', ['email'], unique=True)
    op.create_index(op.f('ix_application_user_id'), 'application_user', ['id'], unique=False)
    op.create_index(op.f('ix_application_user_username'), 'application_user', ['username'], unique=True)
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_timestamp', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('last_modified_timestamp', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('application_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['application_user_id'], ['application_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_admin_id'), 'admin', ['id'], unique=False)
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_timestamp', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('last_modified_timestamp', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('application_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['application_user_id'], ['application_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_client_id'), 'client', ['id'], unique=False)
    op.create_table('feed',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_timestamp', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('last_modified_timestamp', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('published', sa.Boolean(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_feed_id'), 'feed', ['id'], unique=False)
    op.create_table('friendship',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_timestamp', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('last_modified_timestamp', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('friend_id', sa.Integer(), nullable=True),
    sa.Column('requested', sa.Boolean(), nullable=True),
    sa.Column('approved', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.ForeignKeyConstraint(['friend_id'], ['client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_friendship_id'), 'friendship', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_friendship_id'), table_name='friendship')
    op.drop_table('friendship')
    op.drop_index(op.f('ix_feed_id'), table_name='feed')
    op.drop_table('feed')
    op.drop_index(op.f('ix_client_id'), table_name='client')
    op.drop_table('client')
    op.drop_index(op.f('ix_admin_id'), table_name='admin')
    op.drop_table('admin')
    op.drop_index(op.f('ix_application_user_username'), table_name='application_user')
    op.drop_index(op.f('ix_application_user_id'), table_name='application_user')
    op.drop_index(op.f('ix_application_user_email'), table_name='application_user')
    op.drop_table('application_user')
    # ### end Alembic commands ###