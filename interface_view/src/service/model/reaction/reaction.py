from pydantic import BaseModel, ConfigDict, Field


class Reaction(BaseModel):
    id: int
    reaction_url: str

    model_config = ConfigDict(from_attributes=True)