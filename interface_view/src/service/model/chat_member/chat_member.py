from pydantic import BaseModel, ConfigDict


class ChatMember(BaseModel):
    id: int
    user_id: int
    chat_id: int

    model_config = ConfigDict(from_attributes=True)