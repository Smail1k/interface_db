from pydantic import BaseModel, ConfigDict


class ChannelMember(BaseModel):
    id: int
    user_id: int
    channel_id: int

    model_config = ConfigDict(from_attributes=True)