"""empty message

Revision ID: 8c2a2319df7f
Revises: 16183eae08cb
Create Date: 2017-06-24 01:18:24.949078

"""

# revision identifiers, used by Alembic.
revision = '8c2a2319df7f'
down_revision = '16183eae08cb'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event_topics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('slug', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.alter_column('events', 'topic', new_column_name='event_topic_id')
    op.alter_column('events_version', 'topic', new_column_name='event_topic_id')
    op.execute('INSERT INTO event_topics(name, slug) SELECT DISTINCT event_topic_id, lower(replace(regexp_replace(event_topic_id, \'& |,\', \'\', \'g\'), \' \', \'-\'))\
                FROM events where not exists (SELECT 1 FROM event_topics where event_topics.name=events.event_topic_id) and event_topic_id is not null;')
    op.execute('UPDATE events SET event_topic_id = (SELECT id FROM event_topics WHERE event_topics.name=events.event_topic_id)')
    op.execute('ALTER TABLE events ALTER COLUMN event_topic_id TYPE integer USING event_topic_id::integer')
    op.create_foreign_key(None, 'events', 'event_topics', ['event_topic_id'], ['id'], ondelete='CASCADE')
    op.execute('UPDATE events_version SET event_topic_id = (SELECT id FROM event_topics WHERE event_topics.name=events_version.event_topic_id)')
    op.execute('ALTER TABLE events_version ALTER COLUMN event_topic_id TYPE integer USING event_topic_id::integer')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('events_event_topic_id_fkey', 'events', type_='foreignkey')
    op.execute('ALTER TABLE events ALTER COLUMN event_topic_id TYPE varchar USING event_topic_id::varchar')
    op.execute('UPDATE events SET event_topic_id = (SELECT name FROM event_topics WHERE event_topics.id=cast(events.event_topic_id as int))')
    op.execute('ALTER TABLE events_version ALTER COLUMN event_topic_id TYPE varchar USING event_topic_id::varchar')
    op.execute('UPDATE events_version SET event_topic_id = (SELECT name FROM event_topics WHERE event_topics.id=cast(events_version.event_topic_id as int))')
    op.alter_column('events', 'event_topic_id', new_column_name='topic')
    op.alter_column('events_version', 'event_topic_id', new_column_name='topics')
    op.drop_table('event_topics')
    ### end Alembic commands ###
