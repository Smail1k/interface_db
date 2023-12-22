from typing import Sequence
from src.sql.database import conn
from src.service.model.channel_member.channel_member import ChannelMember
from src.service.model.channel_member.channel_member_new import NewChannelMember


def insert_member(member: NewChannelMember):
    with conn.cursor() as curs:
        curs.execute('INSERT INTO t_channel_member'
                     ' (id_user, channel_id)'
                     ' VALUES  (?,?)'), (member.user_id, member.channel_id)
    curs.commit()


def get_all_member_channel(channel_id: int, limit: int = 100,
        offset: int = 0) -> Sequence[ChannelMember]:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_channel_member WHERE channel_id = ?'
                     ' ORDER BY id OFFSET ? ROWS FETCH NEXT ? ROWS ONLY',
                     (channel_id, offset, limit))
        result = curs.fetchall()
    return result


def get_user_all_channel(user_id: int, limit: int = 100,
        offset: int = 0) -> Sequence[int]:
    with conn.cursor() as curs:
        curs.execute('SELECT channel_id FROM t_channel_member WHERE id_user = ?'
                     ' ORDER BY id OFFSET ? ROWS FETCH NEXT ? ROWS ONLY',
                     (user_id, offset, limit))
        result = curs.fetchall()
    return result


def delete_member_from_channel(member_id: int, channel_id: int):
    with conn.cursor() as curs:
        curs.execute('DELETE FROM t_channel_member'
                     ' WHERE id_user = ? AND channel_id = ?',
                     (member_id, channel_id))
    curs.commit()


def delete_member_from_all_channel(member_id: int):
    with conn.cursor() as curs:
        curs.execute('DELETE FROM t_channel_member WHERE id_user = ?'), (member_id, )
    curs.commit()
