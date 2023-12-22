from pydantic import BaseModel, ConfigDict

from src.service.model.attachment.attachment_new import NewAttachment


class NewMessage(BaseModel):
    text: str | None = None
    user_id: int
    chat_id: int
    attachment: NewAttachment | None = None
    attachment_id: int | None = None

    model_config = ConfigDict(from_attributes=True)
