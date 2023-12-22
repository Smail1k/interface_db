from typing import Sequence

from src.service.model.file.picture import Picture
from src.sql.database import conn
from src.service.model.file.video import Video
from src.service.model.file.file_new import NewFile


def insert_picture(file: NewFile) -> Picture:
    with conn.cursor() as curs:
        curs.execute('INSERT INTO t_picture'
                     '(picture_name, picture_url, picture_added_at)'
                     'VALUES (?, ?, GETDATE())',
                     (file.name, file.url))
        curs.commit()
        curs.execute('SELECT * FROM t_picture ORDER BY id')
        result = curs.fetchone()
    return result


def get_all_picture() -> Sequence[Picture]:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_picture',)
        result = curs.fetchall()
    return result


def get_picture_by_id(picture_id: int) -> Picture:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_picture WHERE id =?',
                     (picture_id,))
        result = curs.fetchone()
    return result


def update_picture(picture: Picture):
    with conn.cursor() as curs:
        curs.execute('UPDATE t_picture SET '
                     'picture_name = ?, picture_url = ?'
                     ' WHERE id = ?',
                     (picture.name,
                      picture.url, picture.id))
    curs.commit()


def delete_picture(picture_id: int):
    with conn.cursor() as curs:
        curs.execute('DELETE FROM t_picture WHERE id = ?',
                     (picture_id,))
        curs.commit()


def insert_video(file: NewFile) -> Video:
    with conn.cursor() as curs:
        curs.execute('INSERT INTO t_video'
                     ' (video_name, video_url, video_added_at)'
                     'VALUES (?, ?, GETDATE())',
                     (file.name, file.url))
        curs.commit()
        curs.execute('SELECT * FROM t_video ORDER BY id')
        result = curs.fetchone()
    return result


def get_all_video() -> Sequence[Video]:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_video',)
        result = curs.fetchall()
    return result


def get_video_by_id(video_id: int) -> Video:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_video WHERE id =?',
                     (video_id,))
        result = curs.fetchone()
    return result


def update_video(video: Video):
    with conn.cursor() as curs:
        curs.execute('UPDATE t_video SET '
                     'video_name = ?, video_url = ?'
                     ' WHERE id = ?',
                     (video.name,
                      video.url, video.id))
    curs.commit()


def delete_video(video_id: int):
    with conn.cursor() as curs:
        curs.execute('DELETE FROM t_video WHERE id = ?',
                     (video_id,))
        curs.commit()
