from pydantic import BaseModel, ConfigDict, Field


class Chat(BaseModel):
    id: int
    chat_name: str
    creator_id: int
    admin_id: int | None = None

    model_config = ConfigDict(from_attributes=True)
