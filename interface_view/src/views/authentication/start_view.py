from flet import *
import config


def start(page: Page):
    def admin_on_click(e):
        config.type_field = True
        page.go("/authorization")

    def admin_on_hover(e):
        e.control.bgcolor = "#FF8E00" if e.data == "true" else colors.WHITE
        e.control.content.color = colors.WHITE if e.data == "true" else colors.BLACK
        e.control.update()

    def user_on_click(e):
        config.type_field = False
        page.go("/authorization")

    def user_on_hover(e):
        e.control.bgcolor = "#216EE2" if e.data == "true" else colors.WHITE
        e.control.content.color = colors.WHITE if e.data == "true" else colors.BLACK
        e.control.update()

    page.window_full_screen = False
    page.clean()

    txt_st = Text("Вход", weight=FontWeight.BOLD,
                  size=50, text_align=TextAlign.CENTER)

    type_fields_st = Row(
        alignment=MainAxisAlignment.CENTER,
        width=600,
        height=60,
        controls=[
            Container(
                content=Text("Администратор", color=colors.BLACK, size=18),
                alignment=alignment.center,
                width=300, height=50,
                bgcolor=colors.WHITE,
                border=border.all(width=1, color=colors.BLACK),
                border_radius=border_radius.all(30),
                on_hover=admin_on_hover,
                on_click=admin_on_click,
            ),
            Container(
                content=Text(value="Пользователь", color=colors.BLACK, size=18),
                alignment=alignment.center,
                width=300, height=50,
                bgcolor=colors.WHITE,
                border=border.all(width=1, color=colors.BLACK),
                border_radius=border_radius.all(30),
                on_hover=user_on_hover,
                on_click=user_on_click,
            )
        ]
    )

    img_st = Container(
        content=Image(
            src="../assets/logo.png",
            ),
        width=150,
        height=150,
    )

    start_column = Column(
        controls=[img_st, txt_st, type_fields_st],
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        width=config.width_70,
        spacing=10
    )
    return start_column
