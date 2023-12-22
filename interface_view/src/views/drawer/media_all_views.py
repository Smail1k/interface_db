from flet import *
from config import width_70, server_endpoint
import config
import requests


def media(page: Page):
    page.window_full_screen = False
    page.clean()

    if config.status is True:
        media_dict = requests.get(url=server_endpoint + "/media").json()
    else:
        media_dict = requests.get(url=server_endpoint + "/media/me", params={'token': config.token}).json()

    print(media_dict)
    picture_row = Row(spacing=7)
    picture_column = Column(
        controls=[
            Text(value="Изображения", size=23),
            picture_row
        ],
        spacing=5
    )
    video_row = Row(spacing=7)
    video_column = Column(
        controls=[
            Text(value="Видеозаписи", size=23),
            video_row
        ],
        spacing=5
    )

    for picture in media_dict['picture']:
        picture_row.controls.append(Text(value=picture['name']))

    for video in media_dict['video']:
        video_row.controls.append(Text(value=video['name']))

    media_column = Column(
        controls=[picture_column, video_column],
        spacing=20
    )
    return media_column
