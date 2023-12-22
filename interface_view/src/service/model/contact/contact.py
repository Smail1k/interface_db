from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class Contact(BaseModel):
    id: int
    f_name: str
    l_name: str | None = None
    id_user: int
    user_contact_id: int
    show_number: bool
    contact_last_online: datetime

    model_config = ConfigDict(from_attributes=True)
