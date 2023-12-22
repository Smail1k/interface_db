from typing import Sequence
from src.sql.database import conn
from src.service.model.contact.contact import Contact
from src.service.model.contact.contact_new import NewContact


def insert_contact(contact: NewContact):
    with conn.cursor() as curs:
        curs.execute('INSERT INTO t_contact'
                     '(f_name, l_name, id_user,'
                     ' user_contact_id, show_number, contact_last_online)'
                     'VALUES (?, ?, ?, ?, ?, ?)',
                     (contact.f_name, contact.l_name, contact.user_id,
                      contact.contact_id, contact.show_number, contact.last_online))
        curs.commit()


def get_all_contacts() -> Sequence[Contact]:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_contact')
        result = curs.fetchall()
    return result


def get_user_contacts(user_id: int, limit: int,
                      offset: int = 0) -> Sequence[Contact]:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_contact WHERE id_user = ?'
                     ' ORDER BY id OFFSET ? ROWS FETCH NEXT ? ROWS ONLY',
                     (user_id, offset, limit))
        result = curs.fetchall()
    return result


def get_contact_by_id(user_id: int, contact_id: int) -> Contact:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_contact WHERE user_contact_id = ? and id_user = ?',
                     (contact_id, user_id))
        result = curs.fetchone()
    return result


def get_contact_by_f_name_or_l_name(user_id: int,
                                    f_name: str | None = None, l_name: str | None = None) -> Contact:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_contact WHERE id_user = ?'
                     ' AND (f_name = ? OR l_name = ?)',
                     (user_id, f_name, l_name))
        result = curs.fetchone()
    return result


def update_contact(contact: Contact):
    with conn.cursor() as curs:
        curs.execute('UPDATE t_contact SET f_name = ?, l_name = ?, show_number = ?'
                     ' WHERE id = ?',
                     (contact.f_name, contact.l_name,
                      contact.show_number, contact.id))
    curs.commit()


def delete_contact(contact_id: int):
    with conn.cursor() as curs:
        curs.execute('DELETE FROM t_contact WHERE user_contact_id = ?',
                     (contact_id,))
    curs.commit()
