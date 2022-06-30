from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class BaseData(BaseModel):
    user_id: Optional[UUID]
    film_id: Optional[UUID]


class UserComment(BaseData):
    comment: Optional[str]


class UserFilmLike(BaseData):
    like: bool
