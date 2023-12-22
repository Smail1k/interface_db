from pydantic import BaseModel, ConfigDict


class NewChatMember(BaseModel):
    user_id: int
    chat_id: int

    model_config = ConfigDict(from_attributes=True)