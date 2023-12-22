from flet import *
from config import width_70, server_endpoint
import config
import requests


def chat(page: Page):
    page.window_full_screen = False
    page.clean()

    if config.status is True:
        chat_info = requests.get(url=server_endpoint + "/chats").json()
    else:
        chat_info = requests.get(url=server_endpoint + "/chats/me", params={'token': config.token}).json()
    chat_column = Column(width=width_70, controls=[Text(value="Чаты", size=30)],
                         spacing=10)

    for item in chat_info:
        last_message = requests.get(url=server_endpoint + f"/{item['id']}/message", params={'limit': 1}).json()
        writer_l_m = requests.get(url=server_endpoint + f"/users/{last_message[0]['user_id']}").json()
        chat_column.controls.append(
            Column(
                width=chat_column.width,
                height=50,
                spacing=3,
                controls=[
                    Container(
                        width=chat_column.width,
                        content=Text(value=f"{item['name']}", size=18)
                    ),
                    Container(
                        width=chat_column.width,
                        content=Text(value=f"{writer_l_m['f_name']} {writer_l_m['l_name']}: "
                                           f"{last_message[0]['text']}", max_lines=1, overflow="ellipsis")
                    )
                ]
            )
        )
    return chat_column
