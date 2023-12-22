from flet import *

from config import width_70, height_80


def work(page: Page):
    def on_click(e: ContainerTapEvent):
        match e.control.content.value:
            case "Просмотреть":
                page.go("/select")
            case "Добавить":
                page.go("/insert")
            case "Обновить":
                page.go("/update")
            case "Удалить":
                page.go("/delete")

    def on_hover(e):
        match e.control.content.value:
            case "Просмотреть":
                e.control.bgcolor = "#FFFF00" if e.data == "true" else "#FFD700"
            case "Добавить":
                e.control.bgcolor = "#FF00FF" if e.data == "true" else "#CD00CD"
            case "Обновить":
                e.control.bgcolor = "#00FF00" if e.data == "true" else "#32CD32"
            case "Удалить":
                e.control.bgcolor = "#FF0000" if e.data == "true" else "#DD2222"
        e.control.update()

    page.window_full_screen = False
    page.clean()

    work_row = Row(width=width_70 * 0.9, height=height_80 * 0.8,
                   alignment=MainAxisAlignment.CENTER,
                   vertical_alignment=CrossAxisAlignment.CENTER,
                   spacing=10)

    work_row.controls = [
        Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            width=work_row.width / 2,
            height=work_row.height,
            spacing=10,
            controls=[
                Container(
                    width=work_row.width / 2,
                    height=work_row.height / 2,
                    content=Text("Просмотреть", color=colors.BLACK, size=18),
                    alignment=alignment.center,
                    bgcolor="#FFD700",
                    border=border.all(width=1, color=colors.BLACK),
                    border_radius=border_radius.all(15),
                    on_hover=on_hover,
                    on_click=on_click
                ),
                Container(
                    width=work_row.width / 2,
                    height=work_row.height / 2,
                    content=Text(value="Обновить", color=colors.BLACK, size=18),
                    alignment=alignment.center,
                    bgcolor="#32CD32",
                    border=border.all(width=1, color=colors.BLACK),
                    border_radius=border_radius.all(15),
                    on_hover=on_hover,
                    on_click=on_click
                )
            ]
        ),
        Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            height=work_row.height,
            width=work_row.width / 2,
            spacing=10,
            controls=[
                Container(
                    width=work_row.width / 2,
                    height=work_row.height / 2,
                    content=Text("Добавить", color=colors.BLACK, size=18),
                    alignment=alignment.center,
                    bgcolor="#CD00CD",
                    border=border.all(width=1, color=colors.BLACK),
                    border_radius=border_radius.all(10),
                    on_hover=on_hover,
                    on_click=on_click
                ),
                Container(
                    width=work_row.width / 2,
                    height=work_row.height / 2,
                    content=Text(value="Удалить", color=colors.BLACK, size=18),
                    alignment=alignment.center,
                    bgcolor="#DD2222",
                    border=border.all(width=1, color=colors.BLACK),
                    border_radius=border_radius.all(10),
                    on_hover=on_hover,
                    on_click=on_click
                )
            ]
        ),
    ]

    return work_row
