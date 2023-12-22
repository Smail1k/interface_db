from src.service.model.file.file_new import NewFile
from src.sql import crud_file, crud_attachment
from src.service.model.attachment.attachment_new import NewAttachment
from src.service.model.attachment.attachment import Attachment


# новое вложение
def insert_attachment(attachment: NewAttachment):
    new_attachment = NewAttachment(
        picture_id=attachment.picture_id,
        video_id=attachment.video_id
    )
    return crud_attachment.insert_attachment(attachment=new_attachment)


def get_all_attachment():
    attachments = crud_attachment.get_all_attachment()
    for attachment in attachments:
        attachment = Attachment.model_validate(attachment)
    return attachments


# вложение по id
def get_attachment_by_id(attachment_id: int):
    attachment = crud_attachment.get_attachment_by_id(attachment_id=attachment_id)
    return Attachment.model_validate(attachment)


# обновить вложение
def update_attachment(attachment: Attachment):
    return crud_attachment.update_attachment(attachment=attachment)


# удалить вложение
def delete_attachment(attachment_id: int):
    return crud_attachment.delete_attachment(attachment_id=attachment_id)
