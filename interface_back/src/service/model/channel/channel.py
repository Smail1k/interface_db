from pydantic import BaseModel, ConfigDict, Field


class Channel(BaseModel):
    id: int
    name: str = Field(validation_alias='channel_name')
    creator_id: int
    moderator_id: int | None = None

    model_config = ConfigDict(from_attributes=True)
