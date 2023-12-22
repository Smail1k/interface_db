from flet import *
import config
import requests
from translate import Translator

# Создаем объект переводчика
translator_ru_eng = Translator(from_lang="Russian", to_lang="English")
translator_eng_ru = Translator(from_lang="English", to_lang="Russian")
dict_translate_value = {"пользователи": "users", "чаты": "chats",
                        "каналы": "channels", "сообщения": "messages",
                        "контакты": "contacts", "изображения": "pictures",
                        "видеозаписи": "videos"}


def select(page: Page):
    def create_table(endpoint_value: str, endpoint_value_id: str = None):
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

        table = DataTable(
            width=select_column.width,
            columns=[
            ],
            rows=[
            ],
            horizontal_lines=border.BorderSide(1),
            vertical_lines=border.BorderSide(1),

        )
        if more_table_info:
            keys = more_table_info[0].keys()
            for info in more_table_info:
                temp_row = DataRow(
                    cells=[],
                )
                for value in info.values():
                    temp_row.cells.append(
                        DataCell(content=Text(value=value, expand=False))
                    )
                table.rows.append(temp_row)
        else:
            keys = one_table_info.keys()
            temp_row = DataRow(
                cells=[]
            )
            for value in one_table_info.values():
                temp_row.cells.append(
                    DataCell(content=Text(value=value, expand=False))
                )
            table.rows.append(temp_row)

        index_key = 0
        for key in keys:
            if "id" in key:
                table.columns.append(DataColumn(label=Text(value=f"{key}", expand=True), numeric=True))
            elif key in ("hash_password", "text"):
                for item in table.rows:
                    item.cells[index_key].content.width = 200
                    item.cells[index_key].content.max_lines = 2
                    item.cells[index_key].content.overflow = "ellipsis"
                page.update()
                table.columns.append(DataColumn(label=Text(value=f"{key}", expand=True)))
            elif "_at" in key or "last_online" in key:
                table.columns.append(DataColumn(label=Text(value=f"{key}", expand=True)))
                for item in table.rows:
                    item.cells[index_key].content.value = item.cells[index_key].content.value[:19]
            else:
                table.columns.append(DataColumn(label=Text(value=f"{key}", expand=True)))
            index_key += 1

        if len(select_column.controls) > 2:
            select_column.controls[2] = table
        else:
            select_column.controls.append(table)
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
                dropdown2.options.append(dropdown.Option(f"{ru_value}_id={value['contact_id']}"))
            else:
                dropdown2.options.append(dropdown.Option(f"{ru_value}_id={value['id']}"))
        if len(dropdown_row.controls) > 1:
            dropdown_row.controls[1] = dropdown2
        else:
            dropdown_row.controls.append(dropdown2)

        page.update()

    page.window_full_screen = True

    txt = Text(value="Выберите необходимые данные для просмотра", text_align=alignment.center_left, size=20)
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

    dropdown_row = Row(
        controls=[
            dropdown1
        ],
        spacing=50,
    )

    select_column = Column(
        controls=[txt, dropdown_row],
        alignment=MainAxisAlignment.CENTER,
        width=config.width,
        spacing=10
    )

    return select_column
