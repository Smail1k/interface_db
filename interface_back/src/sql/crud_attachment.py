from typing import Sequence

from src.sql.database import conn
from src.service.model.attachment.attachment import Attachment
from src.service.model.attachment.attachment_new import NewAttachment


def insert_attachment(attachment: NewAttachment) -> Attachment:
    with conn.cursor() as curs:
        curs.execute('INSERT INTO t_attachment (picture_id, video_id) VALUES (?, ?)',
                     (attachment.picture_id, attachment.video_id))
        conn.commit()  # сохраняет изменения
        curs.execute('SELECT * FROM t_attachment ORDER BY id')
        result = curs.fetchone()
    return result


def get_all_attachment():
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_attachment')
        result = curs.fetchall()
        return result


def get_attachment_by_id(attachment_id: id) -> Attachment:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_attachment WHERE id=?', (attachment_id,))
        result = curs.fetchone()
        return result


def update_attachment(attachment: Attachment):
    with conn.cursor() as curs:
        curs.execute('UPDATE t_attachment'
                     ' SET picture_id = ?, video_id = ? WHERE id = ?',
                     (attachment.picture_id,
                      attachment.video_id, attachment.id))
        conn.commit()


def delete_attachment(attachment_id: int):
    with conn.cursor() as curs:
        curs.execute('DELETE FROM t_attachment where id = ?', (attachment_id,))
    conn.commit()
