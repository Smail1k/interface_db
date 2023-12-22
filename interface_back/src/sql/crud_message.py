from typing import Sequence
from src.sql.database import conn
from src.service.model.message.message import Message
from src.service.model.message.message_new import NewMessage


def insert_message(message: NewMessage):
    with conn.cursor() as curs:
        curs.execute('INSERT INTO t_message '
                     '(message_text, id_user, chat_id,'
                     ' attachment_id, created_at, updated_at)'
                     ' VALUES (?, ?, ?, ?, GETDATE(), GETDATE())',
                     (message.text, message.user_id, message.chat_id,
                      message.attachment_id))
        conn.commit()  # сохраняет изменения


def get_all_message() -> Sequence[Message]:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_message')
        result = curs.fetchall()
    return result


def get_all_message_user(user_id: int) -> Sequence[Message]:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_message where id_user = ?',
                     (user_id, ))
        result = curs.fetchall()
    return result


def get_message_of_chat_id(chat_id: int, limit: int,
                           offset: int = 0) -> Sequence[Message]:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_message WHERE chat_id = ?'
                     ' ORDER BY id OFFSET ? ROWS FETCH NEXT ? ROWS ONLY',
                     (chat_id, offset, limit))
        result = curs.fetchall()
    return result


def get_message_by_id(message_id: int) -> Message:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_message WHERE id = ?',
                     (message_id,))
        result = curs.fetchone()
    return result


def update_message(message: Message):
    with conn.cursor() as curs:
        curs.execute('UPDATE t_message SET '
                     'message_text = ?, attachment_id = ?,'
                     ' updated_at = GETDATE()'
                     ' WHERE id = ?',
                     (message.text,
                      message.attachment_id, message.id))
    conn.commit()


def delete_message(message_id: int):
    with conn.cursor() as curs:
        curs.execute('DELETE FROM t_message WHERE id = ?', (message_id,))
    curs.commit()
