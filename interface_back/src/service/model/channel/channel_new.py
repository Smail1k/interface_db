from pydantic import BaseModel, ConfigDict


class NewChannel(BaseModel):
    name: str
    creator_id: int | None = None
    moderator_id: int | None = None

    model_config = ConfigDict(from_attributes=True)