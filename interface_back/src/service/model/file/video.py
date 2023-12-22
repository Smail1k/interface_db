from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class Video(BaseModel):
    id: int
    name: str = Field(validation_alias='video_name')
    url: str = Field(validation_alias='video_url')
    created_at: datetime = Field(validation_alias='video_added_at')

    model_config = ConfigDict(from_attributes=True)