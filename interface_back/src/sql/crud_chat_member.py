from typing import Sequence
from src.sql.database import conn
from src.service.model.chat_member.chat_member import ChatMember
from src.service.model.chat_member.chat_member_new import NewChatMember


def insert_member(member: NewChatMember):
    with conn.cursor() as curs:
        curs.execute('INSERT INTO t_channel_member'
                     ' (id_user, channel_id)'
                     ' VALUES  (?,?)'), (member.user_id, member.channel_id)
    curs.commit()


def get_all_member_chat(chat_id: int, limit: int = 10,
        offset: int = 0) -> Sequence[ChatMember]:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_chat_member WHERE chat_id = ?'
                     ' ORDER BY id OFFSET ? ROWS FETCH NEXT ? ROWS ONLY',
                     (chat_id, offset, limit))
        result = curs.fetchall()
    return result


def get_user_all_chat(user_id: int, limit: int = 100,
        offset: int = 0) -> Sequence[int]:
    with conn.cursor() as curs:
        curs.execute('SELECT chat_id FROM t_chat_member WHERE id_user = ?'
                     ' ORDER BY id OFFSET ? ROWS FETCH NEXT ? ROWS ONLY',
                     (user_id, offset, limit))
        result = curs.fetchall()
    return result


def delete_member_from_chat(member_id: int, chat_id: int):
    with conn.cursor() as curs:
        curs.execute('DELETE FROM t_chat_member'
                     ' WHERE id_user = ? AND chat_id = ?',
                     (member_id, chat_id))
    curs.commit()


def delete_member_from_all_chat(member_id: int):
    with conn.cursor() as curs:
        curs.execute('DELETE FROM t_chat_member WHERE id_user = ?'), (member_id, )
    curs.commit()
