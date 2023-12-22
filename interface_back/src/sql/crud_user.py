from typing import Sequence
from src.sql.database import conn
from src.service.model.user.user import User
from src.service.model.user.user_new import NewUser


def insert_user(user: NewUser) -> User:
    with conn.cursor() as curs:
        curs.execute('INSERT INTO t_user'
            ' (username, f_name, l_name, phone,'
            ' hash_password, registered_at, last_online, status_ad_us)'
            ' VALUES (?, ?, ?, ?, ?, GETDATE(), GETDATE(), ?)',
            (user.username, user.f_name, user.l_name,
             user.phone, user.password, user.status))
        conn.commit()  # сохраняет изменения
        curs.execute('SELECT * FROM t_user ORDER BY id')
        result = curs.fetchone()
    return result


def get_users(limit: int, offset: int = 0) -> Sequence[User]:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_user'
                     ' ORDER BY id OFFSET ? ROWS'
                     ' FETCH NEXT ? ROWS ONLY', (offset, limit))
        result = curs.fetchall()
    return result


def get_user_by_id(user_id: int) -> User:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_user WHERE id=?', (user_id,))
        result = curs.fetchone()
    return result


def get_user_by_username(username: str) -> User:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_user WHERE username=?', (username,))
        result = curs.fetchone()
    return result


def get_user_by_phone(phone: str) -> User:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_user WHERE phone=?', (phone,))
        result = curs.fetchone()
    return result


def get_last_online_by_user_id(user_id: int):
    with conn.cursor() as curs:
        curs.execute('SELECT last_online FROM t_user WHERE id = ?', (user_id,))
        result = curs.fetchone()
    return result


def update_user(user: User):
    with conn.cursor() as curs:
        curs.execute('UPDATE t_user SET '
                     'username = ?, f_name = ?, l_name = ?'
                     ' WHERE id = ?',
                     (user.username, user.l_name,
                      user.f_name, user.id))
    conn.commit()


def update_user_password(user_id: int, password: str):
    with conn.cursor() as curs:
        curs.execute('UPDATE t_user SET hash_password = ?'
                     ' WHERE id = ?', (user_id, password))
    conn.commit()


def update_user_last_online(user_id: int):
    with conn.cursor() as curs:
        curs.execute('UPDATE t_user SET last_online = GETDATE()'
                     ' WHERE id = ?', (user_id, ))
    conn.commit()


def delete_user(user_id: int):
    with conn.cursor() as curs:
        curs.execute('DELETE FROM t_user where id = ?', (user_id, ))
    conn.commit()
