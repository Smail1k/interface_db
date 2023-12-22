from flet import *
import config
import requests
from translate import Translator

from src.service.model.attachment.attachment import Attachment
from src.service.model.channel.channel import Channel
from src.service.model.chat.chat import Chat
from src.service.model.contact.contact import Contact
from src.service.model.file.picture import Picture
from src.service.model.file.video import Video
from src.service.model.message.message import Message
from src.service.model.user.user import User

# Создаем объект переводчика
translator_ru_eng = Translator(from_lang="Russian", to_lang="English")
translator_eng_ru = Translator(from_lang="English", to_lang="Russian")
dict_translate_value = {"пользователи": "users", "чаты": "chats",
                        "каналы": "channels", "сообщения": "messages",
                        "контакты": "contacts", "изображения": "pictures",
                        "видеозаписи": "videos"}
choice_endpoint = ""
table = DataTable()
lst_change_obj = []


def _update(page: Page):
    def on_hover(e):
        e.control.bgcolor = "#00FF00" if e.data == "true" else colors.WHITE
        e.control.content.color = colors.WHITE if e.data == "true" else colors.BLACK
        e.control.update()

    def on_tap(e):
        global lst_change_obj
        if isinstance(e.control.content, Text):
            e.control.content = TextField(value=e.control.content.value, expand=True)
        else:
            e.control.content = Text(value=e.control.content.value, expand=True)
        e.control.update()
        for item in table.rows:
            for cell in item.cells:
                if e.control.content == cell.content:
                    lst_change_obj.append(item.cells)

    def on_change(e: TapEvent):
        input_url = dict_translate_value[choice_endpoint]
        keys = []
        match choice_endpoint:
            case "пользователи":
                keys = User.model_fields.keys()
            case "чаты":
                keys = Chat.model_fields.keys()
            case "каналы":
                keys = Channel.model_fields.keys()
            case "контакты":
                keys = Contact.model_fields.keys()
            case "сообщения":
                keys = Message.model_fields.keys()
            case "вложения":
                keys = Attachment.model_fields.keys()
            case "изображения":
                keys = Picture.model_fields.keys()
            case "видеозаписи":
                keys = Video.model_fields.keys()

        len_ok_resp = 0
        len_bad_resp = 0
        for change_object in lst_change_obj:
            sent_object = {}
            for key, value in zip(keys, change_object):
                sent_object[key] = value.content.value

            url = config.server_endpoint + f"/{input_url}/{sent_object['id']}/change"
            response = requests.put(url=url, json=sent_object)

            if response.status_code == 200:
                len_ok_resp += 1
            else:
                len_bad_resp += 1

        response_ok_txt = Text(
            value=f"{choice_endpoint.title()}"
                  f" успешно обновлены в колличестве: {len_ok_resp}",
            color=colors.GREEN, text_align=TextAlign.CENTER)

        response_bad_txt = Text(
            value=f"{choice_endpoint.title()} не обновлены в колличестве: {len_bad_resp}",
            color=colors.ERROR, text_align=TextAlign.CENTER)

        if len(update_column.controls) > 3:
            update_column.controls[3] = response_ok_txt
        else:
            update_column.controls.append(response_ok_txt)

        if len(update_column.controls) > 4:
            update_column.controls[4] = response_bad_txt
        else:
            update_column.controls.append(response_bad_txt)

        lst_change_obj.clear()
        e.control.bgcolor = colors.WHITE
        e.control.update()
        page.update(

        )
        update_column.controls.pop(4)
        update_column.controls.pop(3)

    def create_table(endpoint_value: str, endpoint_value_id: str = None):
        page.update()
        if endpoint_value_id:
            one_table_info = requests.get(
                url=config.server_endpoint + f"/{endpoint_value}/{endpoint_value_id}",
                params={'token': config.token}).json()
            more_table_info = None
        else:
            one_table_info = None
            if config.status is True:
                more_table_info = requests.get(
                    url=config.server_endpoint + f"/{endpoint_value}").json()
            else:
                more_table_info = requests.get(
                    url=config.server_endpoint + f"/{endpoint_value}/me",
                    params={'token': config.token}).json()

        global table
        table = DataTable(
            data_row_max_height=80,
            columns=[
            ],
            horizontal_lines=border.BorderSide(1),
            vertical_lines=border.BorderSide(1),
            rows=[
            ],
        )

        if more_table_info:
            keys = more_table_info[0].keys()
            for info in more_table_info:
                temp_row = DataRow(
                    cells=[],
                )
                for value in info.values():
                    temp_row.cells.append(
                        DataCell(content=Text(value=value, expand=False),
                                 on_tap=on_tap)
                    )
                table.rows.append(temp_row)
        else:
            keys = one_table_info.keys()
            temp_row = DataRow(
                cells=[]
            )
            for value in one_table_info.values():
                temp_row.cells.append(
                    DataCell(content=Text(value=value, expand=False),
                             on_tap=on_tap)
                )
            table.rows.append(temp_row)

        index_key = 0
        for key in keys:
            if key == "status" and config.status == 0:
                for item in table.rows:
                    item.cells[index_key].on_tap = None
            elif ("id" in key or key == "phone") and key not in ("moderator_id", "admin_id", "attachment_id"):
                table.columns.append(DataColumn(label=Text(value=f"{key}", expand=True), numeric=True))
                for item in table.rows:
                    item.cells[index_key].on_tap = None
            elif key == "hash_password":
                for item in table.rows:
                    item.cells[index_key].on_tap = None
                    item.cells[index_key].content.width = 200
                    item.cells[index_key].content.max_lines = 2
                    item.cells[index_key].content.overflow = "ellipsis"
                table.columns.append(DataColumn(label=Text(value=f"{key}", expand=True)))
            elif "_at" in key or "last_online" in key:
                table.columns.append(DataColumn(label=Text(value=f"{key}", expand=True)))
                for item in table.rows:
                    item.cells[index_key].on_tap = None
                    item.cells[index_key].content.value = item.cells[index_key].content.value[:19]
            else:
                table.columns.append(DataColumn(label=Text(value=f"{key}", expand=True)))
            index_key += 1

        if len(update_column.controls) > 2:
            update_column.controls[2] = table
        else:
            update_column.controls.append(table)
        update_column.controls[1].controls.append(update_button)
        page.update()

    def dropdown2_changed(e):
        if "Все" in dropdown_row.controls[1].value:
            create_table(endpoint_value=dict_translate_value[f'{str(dropdown1.value).lower()}'])
        else:
            index = str(dropdown_row.controls[1].value).rfind("_id")
            choice_until_id = dict_translate_value[f'{str(dropdown1.value).lower()}']
            choice_after_id = str(dropdown_row.controls[1].value)[index + 4:]
            create_table(endpoint_value=choice_until_id, endpoint_value_id=choice_after_id)
        page.update()

    def dropdown1_changed(e):
        global choice_endpoint
        choice_endpoint = dropdown1.value.lower()
        global dict_translate_value
        translate_value = dict_translate_value[f'{str(dropdown1.value).lower()}']
        if config.status is True:
            values = requests.get(
                url=config.server_endpoint + f"/{translate_value}").json()
        else:
            values = requests.get(
                url=config.server_endpoint + f"/{translate_value}/me",
                params={'token': config.token}).json()
        dropdown2 = Dropdown(
            width=200,
            border_radius=10,
            on_change=dropdown2_changed,
            options=[
                dropdown.Option(f"Все {str(dropdown1.value).lower()}"),

            ],
        )
        ru_value = translator_eng_ru.translate(dict_translate_value[f'{str(dropdown1.value).lower()}'][:-1])

        for value in values:
            if ru_value == "контакт":
                continue
            else:
                dropdown2.options.append(dropdown.Option(f"{ru_value}_id={value['id']}"))
        if len(dropdown_row.controls) > 1:
            dropdown_row.controls[1] = dropdown2
        else:
            dropdown_row.controls.append(dropdown2)

        page.update()

    page.window_full_screen = True

    txt = Text(value="Выберите необходимые данные для обноления", text_align=alignment.center_left, size=20)
    dropdown1 = Dropdown(
        width=200,
        border_radius=10,
        on_change=dropdown1_changed,
        options=[
            dropdown.Option("Чаты"),
            dropdown.Option("Каналы"),
            dropdown.Option("Сообщения"),
            dropdown.Option("Контакты"),
            dropdown.Option("Изображения"),
            dropdown.Option("Видеозаписи"),
        ],
    )
    if config.status is True:
        dropdown1.options.insert(0, dropdown.Option("Пользователи"))

    update_button = Container(
        content=Text("Обновить", color=colors.BLACK),
        alignment=alignment.center,
        width=130,
        height=50,
        bgcolor=colors.WHITE,
        border=border.all(width=1, color=colors.BLACK),
        border_radius=border_radius.all(15),
        on_hover=on_hover,
        on_click=on_change
    )

    dropdown_row = Row(
        controls=[
            dropdown1
        ],
        spacing=50,
    )

    update_column = Column(
        controls=[txt, dropdown_row],
        alignment=MainAxisAlignment.CENTER,
        width=config.width,
        spacing=10
    )

    return update_column
