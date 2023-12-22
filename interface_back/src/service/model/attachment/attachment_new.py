from pydantic import BaseModel, ConfigDict


class NewAttachment(BaseModel):
    picture_id: int | None = None
    video_id: int | None = None

    model_config = ConfigDict(from_attributes=True)