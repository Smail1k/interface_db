from fastapi import HTTPException
from starlette import status

from src.service.model.contact.contact import Contact
from src.service.model.contact.contact_new import NewContact
from src.sql import crud_contact, crud_user


# новый контакт
def insert_contact(contact: NewContact):
    if get_contact_by_id(user_id=contact.user_id, contact_id=contact.contact_id) is None:
        contact.last_online = crud_user.get_last_online_by_user_id(contact.contact_id)[0]
        return crud_contact.insert_contact(contact=contact)
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Такой контакт уже существует",
            headers={"WWW-Authenticate": "Bearer"},
        )


# все контакты
def get_all_contact():
    contacts = crud_contact.get_all_contacts()
    for contact in contacts:
        contact = Contact.model_validate(contact)
    return contacts


# все контакты id-пользователя
def get_user_contact(user_id: id, limit: int):
    contacts = crud_contact.get_user_contacts(user_id=user_id, limit=limit)
    for contact in contacts:
        contact = Contact.model_validate(contact)
    return contacts


# id-контакт
def get_contact_by_id(user_id: int, contact_id: int):
    contact = crud_contact.get_contact_by_id(user_id=user_id, contact_id=contact_id)
    if contact:
        contact = Contact.model_validate(contact)
    return contact


# изменение контакта
def update_contact(contact: Contact):
    return crud_contact.update_contact(contact=contact)


# удаление контакта
def delete_contact(contact_id: int):
    return crud_contact.delete_contact(contact_id=contact_id)
