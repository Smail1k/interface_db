from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class Message(BaseModel):
    id: int
    text: str = Field(validation_alias='message_text', default=None)
    created_at: datetime
    updated_at: datetime
    user_id: int = Field(validation_alias='id_user')
    chat_id: int
    attachment_id: int | None = None

    model_config = ConfigDict(from_attributes=True)

