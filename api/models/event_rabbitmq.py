from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class LikeEvent(BaseModel):
    queue_name: Optional[str]
    message_author: Optional[UUID]
    film_id: Optional[UUID]
    user_id: Optional[UUID]
