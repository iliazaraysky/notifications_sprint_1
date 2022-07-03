import aiohttp
from uuid import uuid4
from typing import List
from fastapi import APIRouter, Depends, Request

from api.v1.rabbitmq_api import user_push_publisher
from models.event_rabbitmq import LikeEvent
from models.event_user import UserComment, UserFilmLike, UserCommentLike
from services.user_event_service import (UserEventService,
                                         get_user_event_service)

router = APIRouter()
message_broker_url = 'http://notifications-fastapi:8001/api/v1/rabbitmq/publisher'


@router.get("/{film_id}/comments", response_model=List[UserComment])
async def get_film_comments(
        film_id: str,
        comment_get: UserEventService = Depends(get_user_event_service)
):
    """
    Все комментарии пользователей к фильму
    """
    get_film_comments_list = await comment_get.get_comments_list(film_id)
    return get_film_comments_list


@router.post("/{film_id}/add-comment")
async def user_comment(
        film_id: str,
        data: UserComment,
        comment_post: UserEventService = Depends(get_user_event_service)):
    """
    Добавляет комментарии пользователя к фильму. Обязательные поля:
    - **id**: UUID комментария (генерируется автоматически)
    - **user_id**: UUID пользователя
    - **film_id**: UUID фильма (берется из URL)
    - **comment**: Текст комментария
    """
    data.id = str(uuid4())
    data.film_id = film_id
    user_comment = await comment_post.post_comment(data)

    return user_comment


@router.post("/{film_id}/comments/{comment_id}/like")
async def comment_like(
        film_id: str,
        comment_id: str,
        data: UserCommentLike,
        like_comment: UserEventService = Depends(get_user_event_service)):

    """
    Лайки комментария к фильму. Обязательные поля:
    - **comment_id**: UUID комментария к фильму
    - **user_id**: UUID пользователя
    - **film_id**: UUID фильма
    - **like**: Bool значение. False или True
    После наступления события данные уходят в брокер сообщений
    """

    data.film_id = film_id
    data.comment_id = comment_id
    comment_like = await like_comment.comment_like(data, comment_id)

    # Подготавливаем данные для брокера, и отправляем их в RabbitMQ
    broker = LikeEvent()
    broker.queue_name = str("api-push")
    broker.message_author = str(comment_like['author'])
    broker.film_id = str(film_id)
    broker.user_id = str(data.user_id)
    await user_push_publisher(broker)

    return comment_like


@router.get("/get-likes", response_model=List[UserFilmLike])
async def get_user_like(get_like: UserEventService = Depends(get_user_event_service)):
    """
    Список лайков. Общий.
    """
    get_user_like = await get_like.get_like_list()
    return get_user_like


@router.post("/{film_id}/add-like")
async def user_like(data: UserFilmLike,
                    film_id: str,
                    like_post: UserEventService = Depends(get_user_event_service)):
    """
    Лайки пользователя к фильму. Обязательные поля
    - **user_id**: UUID пользователя
    - **film_id**: UUID фильма
    - **like**: Bool значение. False или True
    """

    data.film_id = film_id
    user_film_like = await like_post.post_like(data)
    return user_film_like
