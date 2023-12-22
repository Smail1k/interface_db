from pydantic import BaseModel, ConfigDict


class NewReactionMessage(BaseModel):
    message_id: int
    user_id: int
    reaction_id: int

    model_config = ConfigDict(from_attributes=True)