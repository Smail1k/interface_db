from pydantic import BaseModel, ConfigDict


class NewReaction(BaseModel):
    url: str

    model_config = ConfigDict(from_attributes=True)