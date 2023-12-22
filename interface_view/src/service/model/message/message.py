from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class Message(BaseModel):
    id: int
    message_text: str | None = None
    created_at: datetime
    updated_at: datetime
    id_user: int
    chat_id: int
    attachment_id: int | None = None

    model_config = ConfigDict(from_attributes=True)

