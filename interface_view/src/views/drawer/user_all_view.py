from datetime import datetime

import requests
from flet import *

from config import server_endpoint, width_70


def user(page: Page):
    page.window_full_screen = False
    page.clean()

    user_info = requests.get(url=server_endpoint + "/users").json()

    users_column = Column(width=width_70, controls=[Text(value="Пользователи", size=30)],
                          spacing=10)
    for item in user_info:
        parts_time = item['last_online'].split(".")
        last_online = int((datetime.now()
                           - datetime.strptime(parts_time[0],
                                               "%Y-%m-%dT%H:%M:%S")).total_seconds() // 60)
        users_column.controls.append(
            Column(
                width=users_column.width,
                height=50,
                spacing=3,
                controls=[
                    Container(
                        width=users_column.width,
                        content=Text(value=f"{item['f_name']} {item['l_name']}", size=18)
                    ),
                    Container(
                        width=users_column.width,
                        content=Text(value=f"был(а) {last_online} минут назад")
                    )
                ]
            )
        )

    return users_column
