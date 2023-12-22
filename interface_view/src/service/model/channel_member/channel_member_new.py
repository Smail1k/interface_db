from pydantic import BaseModel, ConfigDict


class NewChannelMember(BaseModel):
    user_id: int
    channel_id: int

    model_config = ConfigDict(from_attributes=True)