from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class BaseData(BaseModel):
    id: Optional[UUID]
    film_id: Optional[UUID]
    author: Optional[UUID]


class UserComment(BaseData):
    comment: Optional[str]


class UserFilmLike(BaseData):
    like: bool


class UserCommentLike(BaseData):
    user_id: Optional[str]
    comment_id: Optional[UUID]
    like: bool
