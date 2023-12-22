from typing import Sequence
from src.sql.database import conn
from src.service.model.channel.channel import Channel
from src.service.model.channel.channel_new import NewChannel


def insert_channel(channel: NewChannel):
    with conn.cursor() as curs:
        curs.execute('INSERT INTO t_channel'
            ' (channel_name, creator_id, moderator_id, created_at)'
            ' VALUES (?, ?, ?, GETDATE())',
                     (channel.name, channel.creator_id, channel.moderator_id))
        conn.commit()  # сохраняет изменения


def get_all_channel(limit: int = 100, offset: int = 0) -> Sequence[Channel]:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_channel ORDER BY id '
                     'OFFSET ? ROWS FETCH NEXT ? ROWS ONLY',
                     (offset, limit))
        result = curs.fetchall()
    return result


def get_channel_by_id(channel_id: int) -> Channel:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_channel WHERE id=?',
                     (channel_id,))
        result = curs.fetchone()
        return result


def update_channel(channel: Channel):
    with conn.cursor() as curs:
        curs.execute('UPDATE t_channel SET channel_name = ?, moderator_id = ? WHERE id = ?',
                     (channel.name, channel.moderator_id, channel.id))
    conn.commit()


def delete_channel(channel_id: int):
    with conn.cursor() as curs:
        curs.execute('DELETE FROM t_channel where id = ?', (channel_id,))
    conn.commit()
