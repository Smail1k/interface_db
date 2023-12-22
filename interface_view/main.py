from flet import *

from src.views.overall_view import overall, drawer
from src.views.authentication.start_view import start
from src.views.authentication.authorization_view import authorization
from src.views.authentication.registration_view import registration
from src.views.work.delete_view import _delete
from src.views.work.insert_view import _insert
from src.views.work.update_view import _update
from src.views.work_view import work
from src.views.drawer.media_all_views import media
from src.views.drawer.profile_view import profile
from src.views.drawer.user_all_view import user
from src.views.drawer.chat_all_view import chat
from src.views.drawer.channel_all_view import channel
from src.views.drawer.message_all_view import message
from src.views.work.select_view import select
from config import width_70, height_80


def main(page: Page):
    def route_change(route):
        if str(route.route)[1:] == "":
            appbar.leading = Icon(icons.HOME)
            appbar.title = Text("Interface")
        if str(route.route)[1:] == "/work":
            appbar.leading = IconButton(icon=icons.MENU, on_click=show_drawer)
        elif str(route.route)[1:] != "":
            appbar.leading = None
            appbar.title = Text(f"{str(route.route)[1:]}".title())

        page.views.clear()

        match page.route:
            case "/":
                page.views.append(
                    View(
                        route="/",
                        appbar=appbar,
                        controls=[start(page=page)],
                        vertical_alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    ),
                )
            case "/authorization":
                page.views.append(
                    View(
                        route="/",
                        appbar=appbar,
                        controls=[start(page=page)],
                        vertical_alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    ),
                )
                page.views.append(
                    View(
                        route="/authorization",
                        appbar=appbar,
                        controls=[authorization(page=page)],
                        vertical_alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    )
                )
            case "/registration":
                page.views.append(
                    View(
                        route="/authorization",
                        appbar=appbar,
                        controls=[authorization(page=page)],
                        vertical_alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    )
                )
                page.views.append(
                    View(
                        route="/registration",
                        appbar=appbar,
                        controls=[registration(page=page)],
                        vertical_alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    )
                )
            case "/work":
                page.views.append(
                    View(
                        route="/work",
                        appbar=appbar,
                        drawer=drawer(page=page),
                        controls=[work(page=page)],
                        vertical_alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    )
                )
            case "/profile":
                page.views.append(
                    View(
                        route="/work",
                        appbar=appbar,
                        drawer=drawer(page=page),
                        controls=[work(page=page)],
                        vertical_alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    )
                )
                page.views.append(
                    View(
                        route="/profile",
                        appbar=appbar,
                        controls=[profile(page=page)],
                        vertical_alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    )
                )
            case "/users":
                page.views.append(
                    View(
                        route="/work",
                        appbar=appbar,
                        drawer=drawer(page=page),
                        controls=[work(page=page)],
                        vertical_alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    )
                )
                page.views.append(
                    View(
                        route="/users",
                        appbar=appbar,
                        controls=[user(page=page)],
                        scroll=ScrollMode.AUTO
                    )
                )
            case "/chats":
                page.views.append(
                    View(
                        route="/work",
                        appbar=appbar,
                        drawer=drawer(page=page),
                        controls=[work(page=page)],
                        vertical_alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    )
                )
                page.views.append(
                    View(
                        route="/chats",
                        appbar=appbar,
                        controls=[chat(page=page)],
                        scroll=ScrollMode.AUTO
                    )
                )
            case "/channels":
                page.views.append(
                    View(
                        route="/work",
                        appbar=appbar,
                        drawer=drawer(page=page),
                        controls=[work(page=page)],
                        vertical_alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    )
                )
                page.views.append(
                    View(
                        route="/channels",
                        appbar=appbar,
                        controls=[channel(page=page)],
                        scroll=ScrollMode.AUTO
                    )
                )
            case "/messages":
                page.views.append(
                    View(
                        route="/work",
                        appbar=appbar,
                        drawer=drawer(page=page),
                        controls=[work(page=page)],
                        vertical_alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    )
                )
                page.views.append(
                    View(
                        route="/messages",
                        appbar=appbar,
                        controls=[message(page=page)],
                        scroll=ScrollMode.AUTO
                    )
                )
            case "/media":
                page.views.append(
                    View(
                        route="/work",
                        appbar=appbar,
                        drawer=drawer(page=page),
                        controls=[work(page=page)],
                        vertical_alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    )
                )
                page.views.append(
                    View(
                        route="/media",
                        appbar=appbar,
                        controls=[media(page=page)],
                        scroll=ScrollMode.AUTO
                    )
                )
            case "/select":
                page.views.append(
                    View(
                        route="/work",
                        appbar=appbar,
                        drawer=drawer(page=page),
                        controls=[work(page=page)],
                        vertical_alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    )
                )
                page.views.append(
                    View(
                        route="/select",
                        appbar=appbar,
                        controls=[select(page=page)],
                        scroll=ScrollMode.AUTO
                    )
                )
            case "/insert":
                page.views.append(
                    View(
                        route="/work",
                        appbar=appbar,
                        drawer=drawer(page=page),
                        controls=[work(page=page)],
                        vertical_alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    )
                )
                page.views.append(
                    View(
                        route="/insert",
                        appbar=appbar,
                        controls=[_insert(page=page)],
                    )
                )
            case "/update":
                page.views.append(
                    View(
                        route="/work",
                        appbar=appbar,
                        drawer=drawer(page=page),
                        controls=[work(page=page)],
                        vertical_alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    )
                )
                page.views.append(
                    View(
                        route="/update",
                        appbar=appbar,
                        controls=[_update(page=page)],
                        scroll=ScrollMode.AUTO
                    )
                )
            case "/delete":
                page.views.append(
                    View(
                        route="/work",
                        appbar=appbar,
                        drawer=drawer(page=page),
                        controls=[work(page=page)],
                        vertical_alignment=MainAxisAlignment.CENTER,
                        horizontal_alignment=CrossAxisAlignment.CENTER
                    )
                )
                page.views.append(
                    View(
                        route="/delete",
                        appbar=appbar,
                        controls=[_delete(page=page)],
                        scroll=ScrollMode.AUTO
                    )
                )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    def show_drawer(e):
        page.drawer.open = True
        page.drawer.update()

    page.title = "alpha_vers-messenger"

    page.window_width = width_70
    page.window_height = height_80

    page.theme_mode = "light"
    page.splash = ProgressBar(visible=False)

    icon_darklight, confirm_dialog, appbar = overall(page=page)
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


app(target=main,
    assets_dir="assets")

# , view=AppView.WEB_BROWSER
