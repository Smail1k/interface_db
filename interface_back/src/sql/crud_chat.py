from typing import Sequence
from src.sql.database import conn
from src.service.model.chat.chat import Chat
from src.service.model.chat.chat_new import NewChat


def insert_chat(chat: NewChat):
    with conn.cursor() as curs:
        curs.execute('INSERT INTO t_chat'
            ' (chat_name, creator_id, admin_id, created_at)'
            ' VALUES (?, ?, ?, GETDATE())',
                     (chat.name, chat.creator_id, chat.admin_id))
    conn.commit()  # сохраняет изменения


def get_all_chat(limit: int = 100, offset: int = 0) -> Sequence[Chat]:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_chat ORDER BY id'
                     ' OFFSET ? ROWS FETCH NEXT ? ROWS ONLY',
                     (offset, limit))
        result = curs.fetchall()
    return result


def get_chat_by_id(chat_id: int) -> Chat:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_chat WHERE id = ?',
                     (chat_id,))
        result = curs.fetchone()
    return result


def update_chat(chat: Chat):
    with conn.cursor() as curs:
        curs.execute('UPDATE t_chat SET chat_name = ?, admin_id = ? WHERE id = ?',
                     (chat.name, chat.admin_id, chat.id))
    conn.commit()


def delete_chat(chat_id: int):
    with conn.cursor() as curs:
        curs.execute('DELETE FROM t_chat where id = ?', (chat_id,))
    conn.commit()
