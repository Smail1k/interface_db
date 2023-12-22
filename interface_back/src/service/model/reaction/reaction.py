from pydantic import BaseModel, ConfigDict, Field


class Reaction(BaseModel):
    id: int
    url: str = Field(validation_alias='reaction_url')

    model_config = ConfigDict(from_attributes=True)