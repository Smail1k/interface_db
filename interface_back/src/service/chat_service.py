from src.service.model.chat.chat import Chat
from src.service.model.chat.chat_new import NewChat
from src.sql import crud_chat, crud_chat_member, crud_message


# нвоый чат
def create_chat(chat: NewChat):
    return crud_chat.insert_chat(chat)


# все чаты
def get_all_chat():
    chats = crud_chat.get_all_chat()
    for chat in chats:
        chat = Chat.model_validate(chat)
    return chats


# все чаты id-пользователя
def get_all_chat_user(user_id: int, limit: int):
    chats_id = crud_chat_member.get_user_all_chat(user_id=user_id, limit=limit)
    chats = []
    for item in chats_id:
        chats.append(get_chat_by_id(item[0]))
    return chats


# чат id-пользователя
def get_chat_by_id(chat_id):
    chat = crud_chat.get_chat_by_id(chat_id)
    return Chat.model_validate(chat)


# изменение чата
def update_chat(chat: Chat):
    return crud_chat.update_chat(chat=chat)


# удалание чата
def delete_chat(chat_id: int):
    return crud_chat.delete_chat(chat_id=chat_id)
