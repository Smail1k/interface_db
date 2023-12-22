import jwt
from fastapi import APIRouter, HTTPException

from src.service import user_service, contact_service
from src.service.model.user.user import User
from src.service.model.contact.contact import Contact
from config import SECRET_KEY
from src.service.model.user.user_new import NewUser

user_route = APIRouter(tags=["Пользователь"])


# все пользователи
@user_route.get("/users", response_model=list[User])
async def _user(limit: int = 100):
    return user_service.get_users(limit=limit)


# id-пользователь
@user_route.get("/users/{user_id}", response_model=User)
async def user_profile(user_id: int):
    return user_service.get_user_by_id(user_id)


# свой профиль
@user_route.get("/profile", response_model=User)
async def me_profile(token: str):
    # Передаем сам токен и ключ, с помощью которого декодируем данные и вытаскиваем нужную инфу
    user = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

    if user.get('user_id') is None:
        raise HTTPException(status_code=401, detail="Неверные логин и пароль")

    return user_service.get_user_by_id(user.get('user_id'))


# добавленный пользователь
@user_route.post("/users/new_user")
async def new_user(client: NewUser):
    return user_service.insert_user(client)


# изменение id-пользователя
@user_route.put("/users/{user_id}/change")
async def change(user_id: int, up_user: User, token: str = None):
    if token:
        user = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        if user.get('user_id') is None:
            raise HTTPException(status_code=401, detail="Неверные логин и пароль")
        up_user.id = user.get('user_id')
    return user_service.update_user(user=up_user)


@user_route.put("/users/{user_id}/change/password")
async def change_password(user_id: int, token: str, password: str):
    user = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

    if user.get('user_id') is None:
        raise HTTPException(status_code=401, detail="Неверные логин и пароль")
    return user_service.update_user_password(
        user_id=user.get('user_id'), password=password)


# удаление id-пользователя
@user_route.delete("/users/{user_id}/delete")
async def change(user_id: int):
    return user_service.delete_user(user_id=user_id)
