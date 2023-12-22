from pydantic import BaseModel, ConfigDict


class NewChat(BaseModel):
    name: str
    creator_id: int | None = None
    admin_id: int | None = None

    model_config = ConfigDict(from_attributes=True)