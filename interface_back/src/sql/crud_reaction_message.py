from typing import Sequence

from src.sql.database import conn
from src.service.model.reaction_message.reaction_message import ReactionMessage
from src.service.model.reaction_message.reaction_message_new import NewReactionMessage


def insert_reaction_message(reaction_mess: NewReactionMessage):
    with conn.cursor() as curs:
        curs.execute('INSERT INTO t_reaction_message '
                     '(message_id, reaction_id, id_user)'
                     'VALUES (?, ?, ?)',
                     (reaction_mess.message_id, reaction_mess.reaction_id,
                      reaction_mess.user_id))
        conn.commit()  # сохраняет изменения


def get_all_reaction_message(
        message_id: int, limit: int = 100,
        offset: int = 0) -> Sequence[ReactionMessage]:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_reaction_message WHERE id = ?'
                     ' ORDER BY id OFFSET ? ROWS FETCH NEXT ? ROWS ONLY',
                     (message_id, offset, limit))
        result = curs.fetchall()
    return result


def get_user_id_reaction_message(
        message_id: int, user_id) -> ReactionMessage:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_reaction_message'
                     ' WHERE id = ? AND id_user = ?',
                     (message_id, user_id))
        result = curs.fetchone()
    return result


def delete_user_id_reaction_message(messege_id: int, user_id: int):
    with conn.cursor() as curs:
        curs.execute('DELETE FROM t_reaction_message'
                     ' WHERE id = ? AND id_user =?',
                     (messege_id, user_id))
    curs.commit()


def delete_all_reaction_message(messege_id: int):
    with conn.cursor() as curs:
        curs.execute('DELETE FROM t_reaction_message'
                     ' WHERE id = ?', (messege_id, ))
    curs.commit()
