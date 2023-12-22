from pydantic import BaseModel, ConfigDict


class NewFile(BaseModel):
    name: str
    type: str
    url: str

    model_config = ConfigDict(from_attributes=True)