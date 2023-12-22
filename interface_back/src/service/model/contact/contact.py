from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class Contact(BaseModel):
    id: int
    f_name: str
    l_name: str | None = None
    user_id: int = Field(validation_alias='id_user')
    contact_id: int = Field(validation_alias='user_contact_id')
    show_number: bool
    last_online: datetime = Field(validation_alias='contact_last_online')

    model_config = ConfigDict(from_attributes=True)
