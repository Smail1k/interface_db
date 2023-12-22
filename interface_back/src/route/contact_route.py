import jwt
from fastapi import APIRouter, HTTPException

from src.service import contact_service
from src.service.model.contact.contact import Contact
from config import SECRET_KEY
from src.service.model.contact.contact_new import NewContact

contact_route = APIRouter(tags=["Контакт"])


# все контакты
@contact_route.get("/contacts", response_model=list[Contact])
async def user_contact():
    return contact_service.get_all_contact()


# контакты id-пользователя
@contact_route.get("/contacts/me", response_model=list[Contact])
async def user_contact(token: str, limit: int = 10):
    user = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

    if user.get('user_id') is None:
        raise HTTPException(status_code=401, detail="Неверные логин и пароль")

    return contact_service.get_user_contact(user_id=user.get('user_id'), limit=limit)


# id-контакт
@contact_route.get("/contacts/{contact_id}", response_model=Contact)
async def user_contact(token: str, contact_id: int):
    user = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

    if user.get('user_id') is None:
        raise HTTPException(status_code=401, detail="Неверные логин и пароль")
    return contact_service.get_contact_by_id(user_id=user.get('user_id'), contact_id=contact_id)


# добавленный контакт
@contact_route.post("/contacts/new_contact")
async def new_user(contact: NewContact, token: str = None):
    if token:
        user = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        if user.get('user_id') is None:
            raise HTTPException(status_code=401, detail="Неверные логин и пароль")
        contact.user_id = user.get('user_id')
    return contact_service.insert_contact(contact)


# обновление контакта
@contact_route.put("/contacts/{contact_id}/change")
async def change_contact(contact_id: int, contact: Contact, token: str = None):
    if token:
        user = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        if user.get('user_id') is None:
            raise HTTPException(status_code=401, detail="Неверные логин и пароль")
        contact.user_id = user.get('user_id')
    return contact_service.update_contact(contact=contact)


# удаление контакта
@contact_route.delete("/contacts/{contact_id}/delete")
async def change_contact(contact_id: int):
    return contact_service.delete_contact(contact_id=contact_id)
