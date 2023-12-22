from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class Picture(BaseModel):
    id: int
    picture_name: str
    picture_url: str
    picture_added_at: datetime

    model_config = ConfigDict(from_attributes=True)
