from datetime import timedelta

from fastapi import HTTPException
from starlette import status

from src.service.model.user.user import User
from src.service.model.user.user_new import NewUser
from src.service.token_service import (
    get_password_hash, create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES)
from src.sql import crud_user


# новый пользователь
def insert_user(user: NewUser):
    if get_user_by_phone(user.phone) is None:
        user.password = get_password_hash(user.password)
        user = User.model_validate(crud_user.insert_user(user))
        access_token = create_access_token(
            data={"sub": user.username, "user_id": user.id,
              "password": user.hash_password, "phone": user.phone,
                  "status": user.status},
            expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Пользователь с таким телефоном уже зарегистрирован",
            headers={"WWW-Authenticate": "Bearer"},
        )


def create_user(user: NewUser):
    if (get_user_by_phone(phone=user.phone) is None
            and get_user_by_username(username=user.username) is None):
        user.password = get_password_hash(user.password)
        user = crud_user.insert_user(user)
        return {"detail": "Пользователь успешно добавлен"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Пользователь с таким телефоном/username уже зарегистрирован",
            headers={"WWW-Authenticate": "Bearer"},
        )


# пользователи
def get_users(limit: int):
    users = crud_user.get_users(limit=limit)
    for user in users:
        user = User.model_validate(user)
    return users


# пользователь по id
def get_user_by_id(user_id: int):
    user = crud_user.get_user_by_id(user_id=user_id)
    if user:
        user = User.model_validate(user)
    return user


# пользователь по username
def get_user_by_username(username: str):
    user = crud_user.get_user_by_username(username=username)
    if user:
        user = User.model_validate(user)
    return user


def get_user_by_phone(phone: str):
    user = crud_user.get_user_by_phone(phone=phone)
    if user:
        user = User.model_validate(user)
    return user


# изменение данных пользователя
def update_user(user: User):
    return crud_user.update_user(user)


# изменение пароля пользователя
def update_user_password(user_id: int, password: str):
    password = get_password_hash(password)
    user = crud_user.update_user_password(user_id=user_id, password=password)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return create_access_token(
        data={"sub": user.username, "user_id": user.id, "password": user.hashed_password},
        expires_delta=access_token_expires
    )


# обновление времени последней активности
def update_user_last_online(user_id: int):
    return crud_user.update_user_last_online(user_id=user_id)


# удаление пользователя
def delete_user(user_id: int):
    return crud_user.delete_user(user_id=user_id)
