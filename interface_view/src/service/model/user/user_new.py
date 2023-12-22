from pydantic import BaseModel, ConfigDict


class NewUser(BaseModel):
    phone: str
    username: str | None = None
    f_name: str
    l_name: str
    password: str
    status: bool

    model_config = ConfigDict(from_attributes=True)
