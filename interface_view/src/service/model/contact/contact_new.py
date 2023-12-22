from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class NewContact(BaseModel):
    f_name: str
    l_name: str | None = None
    user_id: int
    contact_id: int
    show_number: bool
    last_online: datetime | None = None

    model_config = ConfigDict(from_attributes=True)