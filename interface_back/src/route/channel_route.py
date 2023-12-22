from fastapi import APIRouter, HTTPException
from jose import jwt

from src.service import channel_service
from src.service.model.channel.channel_new import NewChannel
from src.service.model.channel.channel import Channel
from config import SECRET_KEY

channel_route = APIRouter(tags=["Канал"])


# все чаты
@channel_route.get("/channels", response_model=list[Channel])
async def _channel():
    return channel_service.get_all_channel()


# все каналы id пользователя
@channel_route.get("/channels/me", response_model=list[Channel])
async def _channel_user(token: str, limit: int = 10):
    user = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

    if user.get('user_id') is None:
        raise HTTPException(status_code=401, detail="Неверные логин и пароль")
    return channel_service.get_all_channel_user(user_id=user.get('user_id'), limit=limit)


# id-канал
@channel_route.get("/channels/{channel_id}", response_model=Channel)
async def _cha_idt(channel_id: int):
    return channel_service.get_channel_by_id(channel_id)


@channel_route.post("/channels/new_channel")
async def new_chat(channel: NewChannel, token: str = None):
    if token:
        user = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        if user.get('user_id') is None:
            raise HTTPException(status_code=401, detail="Неверные логин и пароль")
        channel.creator_id = user.get('user_id')
    return channel_service.create_channel(channel)


# изменение id-канала
@channel_route.put("/channels/{channel_id}/change")
async def change_channel(channel_id: int, channel: Channel, token: str = None):
    if token:
        user = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        if user.get('user_id') is None:
            raise HTTPException(status_code=401, detail="Неверные логин и пароль")
        channel.creator_id = user.get('user_id')
    return channel_service.update_channel(channel=channel)


# удаление id-канала
@channel_route.delete("/channels/{channel_id}/delete")
async def delete_channel(channel_id: int):
    return channel_service.delete_channel(channel_id=channel_id)
