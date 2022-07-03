from functools import lru_cache

from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorClient

from db.mongodb import get_mongo
from models.event_user import UserComment, UserFilmLike, UserCommentLike


class UserEventService:
    def __init__(self, mongo: AsyncIOMotorClient):
        self.mongo = mongo

    async def post_comment(self, comment: UserComment):
        db = self.mongo.comments
        comment = jsonable_encoder(comment)
        await db['comments'].insert_one(comment)
        return {'comment create': "ok"}

    async def get_comments_list(self, film_id):
        db = self.mongo.comments
        comment = await db['comments'].find(dict(film_id=f'{film_id}')).to_list(100)
        return comment

    async def get_comment_detail(self, comment_id):
        db = self.mongo.comments
        comment = await db['comments'].find(dict(id=f'{comment_id}')).to_list(1)
        return comment

    async def comment_like(self, like: UserCommentLike, comment_id: str):
        comment_data = await self.get_comment_detail(comment_id)
        author = comment_data[0]['author']
        db = self.mongo.comments_likes
        like = jsonable_encoder(like)
        await db['comments_likes'].insert_one(like)

        if like['like'] == True:
            return {'like': 'True',
                    'author': author}
        else:
            return {'like': 'False',
                    'author': author}

    async def get_like_list(self):
        db = self.mongo.likes
        like = await db['likes'].find().to_list(100)
        return like

    async def post_like(self, like: UserFilmLike):
        db = self.mongo.likes
        like = jsonable_encoder(like)
        await db['likes'].insert_one(like)
        return {'message create': 'ok'}


@lru_cache()
def get_user_event_service(
        mongo: AsyncIOMotorClient = Depends(get_mongo)
) -> UserEventService:
    return UserEventService(mongo)
