from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class Video(BaseModel):
    id: int
    video_name: str
    video_url: str
    video_added_at: datetime

    model_config = ConfigDict(from_attributes=True)