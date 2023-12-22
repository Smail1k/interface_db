from pydantic import BaseModel, ConfigDict
from src.service.model.file.picture import Picture
from src.service.model.file.video import Video


class Media(BaseModel):
    picture: list[Picture]
    video: list[Video]

    model_config = ConfigDict(from_attributes=True)
