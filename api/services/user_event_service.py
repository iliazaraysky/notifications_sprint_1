from functools import lru_cache

from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorClient

from db.mongodb import get_mongo
from models.event_user import UserComment, UserFilmLike


class UserEventService:
    def __init__(self, mongo: AsyncIOMotorClient):
        self.mongo = mongo

    async def post_comment(self, comment: UserComment):
        db = self.mongo.comments
        comment = jsonable_encoder(comment)
        await db['comment'].insert_one(comment)
        return {'message create': "ok"}

    async def get_like_list(self):
        db = self.mongo.likes
        likes = await db['like'].find().to_list(100)
        return likes

    async def post_like(self, like: UserFilmLike):
        db = self.mongo.likes
        like = jsonable_encoder(like)
        await db['like'].insert_one(like)
        return {'message create': 'ok'}


@lru_cache()
def get_user_event_service(
        mongo: AsyncIOMotorClient = Depends(get_mongo)
) -> UserEventService:
    return UserEventService(mongo)
