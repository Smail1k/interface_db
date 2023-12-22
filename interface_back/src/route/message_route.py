from fastapi import APIRouter, HTTPException
from jose import jwt

from config import SECRET_KEY
from src.service import message_service
from src.service.model.message.message import Message
from src.service.model.message.message_new import NewMessage

message_route = APIRouter(tags=["Сообщения"])


# все сообщения
@message_route.get("/messages", response_model=list[Message])
async def _message():
    return message_service.get_all_message()


# сообщения id-пользователя
@message_route.get("/messages/me", response_model=list[Message])
async def _message(token: str):
    user = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

    if user.get('user_id') is None:
        raise HTTPException(status_code=401, detail="Неверные логин и пароль")
    return message_service.get_all_message_user(user.get('user_id'))


# сообщение по id
@message_route.get("/messages/{message_id}", response_model=Message)
async def _message_id(message_id: int):
    return message_service.get_message_by_id(message_id)


# сообщения id-чата
@message_route.get("/{chat_id}/message", response_model=list[Message])
async def _message(chat_id: int, limit: int = 10, offset: int = 0):
    return message_service.get_message_by_chat_id(
        chat_id=chat_id, limit=limit, offset=offset)


# новое сообщение
@message_route.post("/messages/new_message")
async def _new_message(message: NewMessage, token: str = None):
    if token:
        user = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        if user.get('user_id') is None:
            raise HTTPException(status_code=401, detail="Неверные логин и пароль")
        message.user_id = user.get('user_id')
    return message_service.create_message(message)


# изменение сообщения
@message_route.put("/messages/{message_id}/change")
async def update_message(message_id: int, message: Message, token: str = None):
    if token:
        user = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        if user.get('user_id') is None:
            raise HTTPException(status_code=401, detail="Неверные логин и пароль")
        message.user_id = user.get('user_id')
    return message_service.update_message(message=message)


@message_route.delete("/messages/{message_id}/delete")
async def delete_message(message_id: int):
    return message_service.delete_message(message_id=message_id)
