from pydantic import BaseModel, ConfigDict, Field


class Channel(BaseModel):
    id: int
    channel_name: str
    creator_id: int
    moderator_id: int | None = None

    model_config = ConfigDict(from_attributes=True)
