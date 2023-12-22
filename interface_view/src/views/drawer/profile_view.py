from flet import *
from datetime import datetime
from config import width_70, server_endpoint
import config
import requests


def profile(page: Page):
    page.window_full_screen = False
    page.clean()

    profile_info = requests.get(url=server_endpoint + "/profile",
                                params={'token': config.token}).json()

    fl_txt = Text(value=f'{profile_info['f_name']} {profile_info['l_name']}', size=40, text_align=alignment.center)
    usr_txt = Container(content=Text(value=f'@{profile_info['username']}', size=25, text_align=alignment.center),
                        alignment=alignment.center)

    contacts_column = Column(width=width_70 / 3 * 0.8, controls=[Text(value="Контакты", width=width_70 / 3 * 0.8, size=23)],
                             spacing=7)
    chats_column = Column(width=width_70 / 3 * 0.8, controls=[Text(value="Чаты", width=width_70 / 3 * 0.8, size=23)],
                          spacing=7)
    channels_column = Column(width=width_70 / 3 * 0.8, controls=[Text(value="Каналы", width=width_70 / 3 * 0.8, size=23)],
                             spacing=7)

    count = 0
    contacts = requests.get(url=server_endpoint + f"/contacts/me", params={'token': config.token}).json()
    for contact in contacts:
        if count == 4:
            chats_column.controls.append(
                Text(value="...........", size=18)
            )
            break
        count += 1
        parts_time = contact['last_online'].split(".")
        last_online = int((datetime.now()
                           - datetime.strptime(parts_time[0],
                                               "%Y-%m-%dT%H:%M:%S")).total_seconds() // 60)
        contacts_column.controls.append(
            Column(
                width=contacts_column.width,
                height=50,
                spacing=3,
                controls=[
                    Container(
                        width=contacts_column.width,
                        content=Text(value=f"{contact['f_name']} {contact['l_name']}", size=18)
                    ),
                    Container(
                        width=contacts_column.width,
                        content=Text(value=f"был(а) {last_online} минут назад")
                    )
                ]
            )
        )
    count = 0
    chats = requests.get(url=server_endpoint + f"/chats/me", params={'token': config.token}).json()
    for chat in chats:
        if count == 4:
            chats_column.controls.append(
                Text(value="...........", size=18)
            )
            break
        count += 1
        last_message = requests.get(url=server_endpoint + f"/{chat['id']}/message", params={'limit': 1}).json()
        writer_l_m = requests.get(url=server_endpoint + f"/users/{last_message[0]['user_id']}").json()
        chats_column.controls.append(
            Column(
                width=chats_column.width,
                height=50,
                spacing=3,
                controls=[
                    Container(
                        width=chats_column.width,
                        content=Text(value=f"{chat['name']}", size=18)
                    ),
                    Container(
                        width=chats_column.width,
                        content=Text(value=f"{writer_l_m['f_name']} {writer_l_m['l_name']}: "
                                           f"{last_message[0]['text']}", max_lines=1, overflow="ellipsis")
                    )
                ]
            )
        )
    count = 0
    channels = requests.get(url=server_endpoint + f"/channels/me", params={'token': config.token}).json()
    for channel in channels:
        if count == 4:
            channels_column.controls.append(
                Text(value="...........", size=18)
            )
            break
        count += 1
        creator = requests.get(url=server_endpoint + f"/users/{channel['creator_id']}").json()
        channels_column.controls.append(
            Column(
                width=channels_column.width,
                height=50,
                spacing=3,
                controls=[
                    Container(
                        width=channels_column.width,
                        content=Text(value=f"{channel['name']}", size=18)
                    ),
                    Container(
                        width=channels_column.width,
                        content=Text(value=f"Создатель: {creator['f_name']} {creator['l_name']}")
                    )
                ]
            )
        )

    info_row = Row(controls=[contacts_column, chats_column, channels_column],
                   alignment=MainAxisAlignment.SPACE_AROUND)

    profile_column = Column(
        controls=[fl_txt, usr_txt, info_row],
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        width=width_70,
        spacing=10
    )

    return profile_column
