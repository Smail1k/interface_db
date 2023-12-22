from pydantic import BaseModel, ConfigDict


class Attachment(BaseModel):
    id: int
    picture_id: int | None = None
    video_id: int | None = None

    model_config = ConfigDict(from_attributes=True)