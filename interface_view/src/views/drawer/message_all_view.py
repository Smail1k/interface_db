from flet import *
from config import width_70, server_endpoint
import config
import requests


def message(page: Page):
    page.window_full_screen = False
    page.clean()

    if config.status is True:
        message_info = requests.get(url=server_endpoint + "/messages").json()
    else:
        message_info = requests.get(url=server_endpoint + "/messages/me", params={'token': config.token}).json()
    message_column = Column(width=width_70, controls=[Text(value="Сообщения", size=25)],
                            spacing=6)

    for item in message_info:
        writer_l_m = requests.get(url=server_endpoint + f"/users/{item['user_id']}").json()
        message_column.controls.append(
            Column(
                width=message_column.width,
                height=30,
                controls=[
                    Container(
                        width=message_column.width,
                        content=Text(value=f"{writer_l_m['l_name']} {writer_l_m['f_name']}: "
                                           f"{item['text']}", max_lines=2, overflow="ellipsis", size=16)
                    )
                ]
            )
        )
    return message_column
