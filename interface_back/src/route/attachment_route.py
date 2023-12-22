import jwt
from fastapi import APIRouter, HTTPException

from src.service import contact_service, attachment_service
from src.service.model.attachment.attachment import Attachment
from config import SECRET_KEY
from src.service.model.attachment.attachment_new import NewAttachment

attachment_route = APIRouter(tags=["Вложение"])


# добавленное вложение
@attachment_route.post("/attachments/new_attachment", response_model=Attachment)
async def new_attachment(attachment: NewAttachment):
    return attachment_service.insert_attachment(attachment=attachment)


# все вложения
@attachment_route.get("/attachments", response_model=list[Attachment])
async def _attachment():
    return attachment_service.get_all_attachment()


# id-вложение
@attachment_route.get("/attachments/{attachment_id}", response_model=Attachment)
async def _attachment_id(attachment_id: int):
    return attachment_service.get_attachment_by_id(attachment_id=attachment_id)


# изменение вложения
@attachment_route.put("/attachments/{attachment_id}/change")
async def change_attachment(attachment_id: int, attachment: Attachment):
    return attachment_service.update_attachment(attachment=attachment)


# удаление вложения
@attachment_route.delete("/attachments/{attachment_id}/delete")
async def delete_attachment(attachment_id: int):
    return attachment_service.delete_attachment(attachment_id=attachment_id)