from src.service.model.message.message import Message
from src.service.model.message.message_new import NewMessage
from src.sql import crud_message
from src.service import attachment_service


# новое сообщение
def create_message(message: NewMessage):
    if message.attachment:
        message.attachment_id =\
            attachment_service.insert_attachment(message.attachment)
    return crud_message.insert_message(message=message)


def get_all_message():
    messages = crud_message.get_all_message()
    for message in messages:
        message = Message.model_validate(message)
    return messages


def get_all_message_user(user_id: int):
    messages = crud_message.get_all_message_user(user_id)
    for message in messages:
        message = Message.model_validate(message)
    return messages


def get_message_by_chat_id(chat_id: int, limit: int, offset: int):
    messages = crud_message.get_message_of_chat_id(chat_id=chat_id, limit=limit, offset=offset)
    for message in messages:
        message = Message.model_validate(message)
    return messages


def get_message_by_id(message_id: int):
    message = crud_message.get_message_by_id(message_id=message_id)
    return Message.model_validate(message)


def update_message(message: Message):
    return crud_message.update_message(message=message)


def delete_message(message_id: int):
    return crud_message.delete_message(message_id=message_id)
