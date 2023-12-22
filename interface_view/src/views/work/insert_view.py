import pymorphy3
from flet import *
import config
import requests
from translate import Translator

from src.service.model.channel.channel_new import NewChannel
from src.service.model.chat.chat_new import NewChat
from src.service.model.contact.contact_new import NewContact
from src.service.model.file.file_new import NewFile
from src.service.model.message.message_new import NewMessage
from src.service.model.user.user_new import NewUser
from src.service.model.attachment.attachment_new import NewAttachment

# Создаем объект переводчика
translator_ru_eng = Translator(from_lang="Russian", to_lang="English")
translator_eng_ru = Translator(from_lang="English", to_lang="Russian")
dict_translate_value = {"пользователь": "user", "чат": "chat",
                        "канал": "channel", "сообщение": "message",
                        "вложение": "attachment",
                        "контакт": "contact", "медиа": "media"}
choice_endpoint = ""
keys = []

def _insert(page: Page):
    def on_hover(e):
        e.control.bgcolor = "#FF00FF" if e.data == "true" else colors.WHITE
        e.control.content.color = colors.WHITE if e.data == "true" else colors.BLACK
        e.control.update()

    def on_add(e: TapEvent):
        new_object = {}
        global keys
        for index, item in enumerate(keys):
            new_object[f'{item}'] = insert_column.controls[2].controls[0].rows[0].cells[index].content.value
            if new_object[f'{item}'] == '':
                new_object.pop(f'{item}')
        input_url = dict_translate_value[choice_endpoint]
        if choice_endpoint == "медиа":
            url = config.server_endpoint + f"/{input_url}/new_{input_url}"
        else:
            url = config.server_endpoint + f"/{input_url}s/new_{input_url}"

        if config.status is True:
            response = requests.post(url=url, json=new_object)
        else:
            response = requests.post(url=url, json=new_object, params={'token': config.token})

        if response.status_code == 200:
            if choice_endpoint in ("пользователь", "чат", "канал"):
                response_txt = Text(value=f"{choice_endpoint.title()} успешно добавлен",
                                    color=colors.GREEN, text_align=TextAlign.CENTER)
            else:
                response_txt = Text(value=f"{choice_endpoint.title()} успешно добавлено",
                                    color=colors.GREEN, text_align=TextAlign.CENTER)
        else:
            response_txt = Text(value=response.json()['detail'],
                                color=colors.ERROR, text_align=TextAlign.CENTER)

        if len(insert_column.controls) > 3:
            insert_column.controls[3] = response_txt
        else:
            insert_column.controls.append(response_txt)

        e.control.bgcolor = colors.WHITE
        e.control.update()

    def create_table(endpoint_value: str):
        if choice_endpoint == "пользователь":
            morph = pymorphy3.MorphAnalyzer()
            declension_value = morph.parse(choice_endpoint)[0].inflect({'gent'}).word
        else:
            declension_value = endpoint_value.lower()

        if len(dropdown_row.controls) > 1:
            dropdown_row.controls[1] = Text(value=f"добавить {declension_value}", size=20)
        else:
            dropdown_row.controls.append(Text(value=f"добавить {declension_value}", size=20))

        table = DataTable(
            expand=9,
            data_row_max_height=80,
            columns=[
            ],
            horizontal_lines=border.BorderSide(1),
            vertical_lines=border.BorderSide(1),
            rows=[
                DataRow(
                    cells=[
                    ]
                )
            ],
        )

        global keys
        keys = None
        match choice_endpoint:
            case "пользователь":
                keys = NewUser.model_fields.keys()
            case "чат":
                keys = NewChat.model_fields.keys()
            case "канал":
                keys = NewChannel.model_fields.keys()
            case "контакт":
                keys = NewContact.model_fields.keys()
            case "сообщение":
                keys = NewMessage.model_fields.keys()
            case "вложение":
                keys = NewAttachment.model_fields.keys()
            case "медиа":
                keys = NewFile.model_fields.keys()

        for key in keys:
            if key in ("creator_id", "user_id", "attachment_id") and config.status is False:
                continue
            table.columns.append(DataColumn(label=Text(value=key)))
            table.rows[0].cells.append(DataCell(
                TextField(label=f"{key}", height=60,
                          multiline=True, max_lines=2)))

        if len(table_row.controls) != 0:
            table_row.controls[0] = table
        else:
            table_row.controls.append(table)
            table_row.controls.append(add_button)
        return

    def dropdown1_changed(e):
        global choice_endpoint
        choice_endpoint = dropdown1.value.lower()
        create_table(endpoint_value=dropdown1.value)
        page.update()

    page.window_full_screen = True
    txt = Text(value="Выберите необходимые данные для добавления", text_align=alignment.center_left, size=20)

    table_row = Row(
        width=config.width,
        controls=[],
    )

    add_button = Container(
        content=Text("Добавить", color=colors.BLACK),
        alignment=alignment.center,
        expand=1,
        height=40,
        bgcolor=colors.WHITE,
        border=border.all(width=1, color=colors.BLACK),
        border_radius=border_radius.all(15),
        on_click=on_add,
        on_hover=on_hover
    )

    dropdown1 = Dropdown(
        width=200,
        border_radius=10,
        on_change=dropdown1_changed,
        options=[
            dropdown.Option("Чат"),
            dropdown.Option("Канал"),
            dropdown.Option("Контакт"),
            dropdown.Option("Сообщение"),
            dropdown.Option("Медиа"),
        ],
    )

    if config.status is True:
        dropdown1.options.insert(0, dropdown.Option("Пользователь"))
        dropdown1.options.insert(5, dropdown.Option("Вложение"))

    dropdown_row = Row(
        controls=[
            dropdown1
        ],
        spacing=50,
    )

    insert_column = Column(
        controls=[txt, dropdown_row, table_row],
        width=config.width,
        spacing=15
    )

    return insert_column
