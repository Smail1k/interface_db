from pydantic import BaseModel, ConfigDict, Field


class Chat(BaseModel):
    id: int
    name: str = Field(validation_alias='chat_name')
    creator_id: int
    admin_id: int | None = None

    model_config = ConfigDict(from_attributes=True)
