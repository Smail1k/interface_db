from fastapi import APIRouter, HTTPException
from jose import jwt

from src.service import chat_service, message_service
from src.service.model.chat.chat_new import NewChat
from src.service.model.message.message_new import NewMessage
from src.service.model.chat.chat import Chat
from src.service.model.message.message import Message
from config import SECRET_KEY

chat_route = APIRouter(tags=["Чат"])


@chat_route.post("/chats/new_chat")
async def new_chat(chat: NewChat, token: str = None):
    if token:
        user = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        if user.get('user_id') is None:
            raise HTTPException(status_code=401, detail="Неверные логин и пароль")
        chat.creator_id = user.get('user_id')
    return chat_service.create_chat(chat)


# все чаты
@chat_route.get("/chats", response_model=list[Chat])
async def _chat():
    return chat_service.get_all_chat()


# все чаты id пользователя
@chat_route.get("/chats/me", response_model=list[Chat])
async def _chat_user(token: str, limit: int = 10):
    user = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

    if user.get('user_id') is None:
        raise HTTPException(status_code=401, detail="Неверные логин и пароль")
    return chat_service.get_all_chat_user(user_id=user.get('user_id'), limit=limit)


# id-чат
@chat_route.get("/chats/{chat_id}", response_model=Chat)
async def _chat_id(chat_id: int):
    return chat_service.get_chat_by_id(chat_id)


# изменение id-чата
@chat_route.put("/chats/{chat_id}/change")
async def change_chat(chat_id: int, chat: Chat, token: str = None):
    if token:
        user = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        if user.get('user_id') is None:
            raise HTTPException(status_code=401, detail="Неверные логин и пароль")
        chat.creator_id = user.get('user_id')
    return chat_service.update_chat(chat=chat)


# удаление id-чата
@chat_route.delete("/chats/{chat_id}/delete")
async def change_chat(chat_id: int):
    return chat_service.delete_chat(chat_id=chat_id)
