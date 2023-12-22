import requests
from flet import *
from time import sleep

import config


def registration(page: Page):
    def enter(e: ContainerTapEvent):
        def close_dlg(e):
            dlg.open = False
            page.update()

        if not phone_reg.value:
            phone_reg.error_text = "Пожалуйста, введите телефон"
            page.update()
            return
        else:
            phone_reg.error_text = None
            page.update()

        if not password_reg.value:
            password_reg.error_text = "Пожалуйста, введите пароль"
            page.update()
            return
        else:
            password_reg.error_text = None
            page.update()

        if not name_reg.value:
            name_reg.error_text = "Пожалуйста, введите имя"
            name_reg.update()
            return
        else:
            name_reg.error_text = None
            page.update()

        if not last_name_reg.value:
            last_name_reg.error_text = "Пожалуйста, введите фамилию"
            page.update()
            return
        else:
            last_name_reg.error_text = None
            page.update()

        response = requests.post(url=config.server_endpoint + "/registration",
                                 json={'phone': phone_reg.value, 'username': username_reg.value,
                                       'f_name': name_reg.value, 'l_name': last_name_reg.value,
                                       'password': password_reg.value, 'status': config.type_field})
        if response.status_code == 200:
            config.token = response.json()['access_token']
            dlg = AlertDialog(title=Text(value="Успешно", color=colors.GREEN), content=Text(
                value="Добро пожаловать!", text_align=TextAlign.CENTER, size=25))
            page.dialog = dlg
            dlg.open = True
            page.update()
            sleep(1)
            config.token = response.json()['access_token']
            config.status = requests.get(url=config.server_endpoint + f"/profile",
                                         params={'token': config.token}).json()['status']
            page.go("/work")
        elif response.status_code == 401:
            dlg = AlertDialog(title=Text(value="Ошибка 401", color=colors.ERROR, text_align=TextAlign.LEFT),
                              content=Text(
                                  value="Пользователь с таким номером телефона уже зарегистрирован",
                                  text_align=TextAlign.LEFT,
                                  size=20), actions=[TextButton(text="Ок", on_click=close_dlg)],
                              actions_alignment=MainAxisAlignment.END)
            page.dialog = dlg
            dlg.open = True
            page.update()
        else:
            dlg = AlertDialog(title=Text(value=f"Ошибка {response.status_code}", color=colors.ERROR, text_align=TextAlign.LEFT),
                              content=Text(value="Что-то пошло не так...", text_align=TextAlign.LEFT, size=20),
                              actions=[TextButton(text="Ок", on_click=close_dlg)],
                              actions_alignment=MainAxisAlignment.END)
            page.dialog = dlg
            dlg.open = True
            page.update()

    page.window_full_screen = False
    page.clean()

    phone_reg = TextField(label="Phone", width=250, border_radius=8, keyboard_type=KeyboardType.PHONE, max_length=11)
    username_reg = TextField(label="Username", width=250, border_radius=8, helper_text="Вы можете оставить поле пустым")
    name_reg = TextField(label="Name", width=250, border_radius=8)
    last_name_reg = TextField(label="Last_Name", width=250, border_radius=8)
    password_reg = TextField(label="Password", width=250,
                             border_radius=8, password=True, can_reveal_password=True)
    registering_reg = Container(content=TextButton(text="Зарегистрироваться"), on_click=enter)

    registering_column = Column(
        controls=[phone_reg, username_reg, name_reg, last_name_reg, password_reg, registering_reg],
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        width=config.width_70,
        spacing=20
    )

    return registering_column
