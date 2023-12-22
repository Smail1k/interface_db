import requests
from flet import *
from math import pi
import config


def drawer(page: Page):
    def on_hover(e):
        if page.theme_mode == "light":
            e.control.bgcolor = "#d8e2f7" if e.data == "true" else page.bgcolor
        else:
            e.control.bgcolor = "#3c4757" if e.data == "true" else page.bgcolor

        match e.control.content.controls[1].value:
            case "Профиль":
                if e.data == "true":
                    if page.theme_mode == "light":
                        e.control.content.controls[0].src = "../assets/person_hover.png"
                    else:
                        e.control.content.controls[0].color = None
                        e.control.content.controls[0].src = "../assets/person_inv_hover.png"
                else:
                    if page.theme_mode == "light":
                        e.control.content.controls[0].src = "../assets/person.png"
                    else:
                        e.control.content.controls[0].color = colors.WHITE
                        e.control.content.controls[0].src = "../assets/person.png"
            case "Пользователи":
                e.control.content.controls[0].name = icons.SUPERVISED_USER_CIRCLE \
                    if e.data == "true" else icons.SUPERVISED_USER_CIRCLE_OUTLINED
            case "Чаты":
                e.control.content.controls[0].name = icons.CHAT \
                    if e.data == "true" else icons.CHAT_OUTLINED
            case "Каналы":
                e.control.content.controls[0].name = icons.CHAT_BUBBLE \
                    if e.data == "true" else icons.CHAT_BUBBLE_OUTLINE
            case "Сообщения":
                e.control.content.controls[0].name = icons.MESSAGE \
                    if e.data == "true" else icons.MESSAGE_OUTLINED
            case "Медиа":
                e.control.content.controls[0].name = icons.PERM_MEDIA \
                    if e.data == "true" else icons.PERM_MEDIA_OUTLINED

        page.update()

    def on_click(e: ContainerTapEvent):
        match e.control.content.controls[1].value:
            case "Профиль":
                page.go("/profile")
            case "Пользователи":
                page.go("/users")
            case "Чаты":
                page.go("/chats")
            case "Каналы":
                page.go("/channels")
            case "Сообщения":
                page.go("/messages")
            case "Медиа":
                page.go("/media")

    page.window_full_screen = False

    users_container = Container(
        content=Row(
            controls=[Icon(name=icons.SUPERVISED_USER_CIRCLE_OUTLINED),
                      Text(value="Пользователи")]
        ),
        on_click=on_click,
        on_hover=on_hover,
        padding=padding.only(left=30, top=25, bottom=20)
    )

    message_container = Container(
        content=Row(
            controls=[Icon(name=icons.MESSAGE_OUTLINED),
                      Text(value="Сообщения")]
        ),
        on_click=on_click,
        on_hover=on_hover,
        padding=padding.only(left=30, top=25, bottom=20)
    )

    my_drawer = NavigationDrawer(
        controls=[
            Container(
                content=Row(
                    controls=[Image(src="../assets/person.png"),
                              Text(value="Профиль")]
                ),
                on_click=on_click,
                on_hover=on_hover,
                padding=padding.only(left=25, top=25, bottom=20)
            ),
            Container(
                content=Row(
                    controls=[Icon(name=icons.CHAT_OUTLINED),
                              Text(value="Чаты")],
                ),
                on_click=on_click,
                on_hover=on_hover,
                padding=padding.only(left=30, top=25, bottom=20)
            ),
            Container(
                content=Row(
                    controls=[Icon(name=icons.CHAT_BUBBLE_OUTLINE),
                              Text(value="Каналы")],
                ),
                on_click=on_click,
                on_hover=on_hover,
                padding=padding.only(left=30, top=25, bottom=20)
            ),
            Container(
                content=Row(
                    controls=[Icon(name=icons.PERM_MEDIA_OUTLINED),
                              Text(value="Медиа")],
                ),
                on_click=on_click,
                on_hover=on_hover,
                padding=padding.only(left=30, top=25, bottom=20)
            )
        ],
    )

    if config.status is True:
        my_drawer.controls.insert(1, users_container)
        my_drawer.controls.insert(4, message_container)

    return my_drawer


def overall(page: Page):
    def change_theme(e):
        page.splash.visible = True
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        if page.views[0].drawer:
            page.views[0].drawer.controls[0].content.controls[0].color = colors.WHITE \
                if page.theme_mode == "dark" else colors.BLACK
        page.update()
        icon_darklight.selected = not icon_darklight.selected
        page.splash.visible = False
        page.update()

    def check_exit_clicked(e):
        e.control.checked = not e.control.checked
        page.dialog = confirm_dialog
        confirm_dialog.open = True
        page.update()

    def yes_click_confirm(e):
        page.window_destroy()

    def no_click_confirm(e):
        confirm_dialog.open = False
        page.update()

    icon_darklight = IconButton(
        on_click=change_theme,
        icon="dark_mode",
        selected_icon="light_mode",
        style=ButtonStyle(
            color={"": colors.BLACK, "selected": colors.WHITE}
        )
    )

    appbar = AppBar(
        center_title=False,
        bgcolor=colors.SURFACE_VARIANT,
        actions=[
            icon_darklight,
            IconButton(icons.FILTER_3),
            PopupMenuButton(
                items=[
                    PopupMenuItem(
                        text="Выход", checked=False, on_click=check_exit_clicked
                    ),
                ], rotate=pi / 2
            ),
        ],
    )

    confirm_dialog = AlertDialog(
        modal=True,
        title=Text("Пожалуйста, подтвердите"),
        content=Text("Вы действительно хотите выйти?"),
        actions=[
            ElevatedButton("Да", on_click=yes_click_confirm),
            OutlinedButton("Нет", on_click=no_click_confirm),
        ],
        actions_alignment=MainAxisAlignment.END,
    )

    return icon_darklight, confirm_dialog, appbar
