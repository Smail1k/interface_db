from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class User(BaseModel):
    id: int
    phone: str
    username: str | None = None
    f_name: str
    l_name: str
    hash_password: str
    registered_at: datetime
    last_online: datetime
    status: bool = Field(validation_alias='status_ad_us')

    model_config = ConfigDict(from_attributes=True)
