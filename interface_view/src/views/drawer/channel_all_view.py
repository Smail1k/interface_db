from flet import *
from config import width_70, server_endpoint
import config
import requests


def channel(page: Page):
    page.window_full_screen = False
    page.clean()

    if config.status is True:
        channel_info = requests.get(url=server_endpoint + "/channels").json()
    else:
        channel_info = requests.get(url=server_endpoint + "/channels/me", params={'token': config.token}).json()

    channel_column = Column(width=width_70, controls=[Text(value="Каналы", size=30)],
                            spacing=10)
    for item in channel_info:
        creator = requests.get(url=server_endpoint + f"/users/{item['creator_id']}").json()
        channel_column.controls.append(
            Column(
                width=channel_column.width,
                height=50,
                spacing=3,
                controls=[
                    Container(
                        width=channel_column.width,
                        content=Text(value=f"{item['name']}", size=18)
                    ),
                    Container(
                        width=channel_column.width,
                        content=Text(value=f"Создатель: {creator['f_name']} {creator['l_name']}")
                    )
                ]
            )
        )
    return channel_column
