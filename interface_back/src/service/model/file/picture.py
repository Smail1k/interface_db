from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class Picture(BaseModel):
    id: int
    name: str = Field(validation_alias='picture_name')
    url: str = Field(validation_alias='picture_url')
    created_at: datetime = Field(validation_alias='picture_added_at')

    model_config = ConfigDict(from_attributes=True)
