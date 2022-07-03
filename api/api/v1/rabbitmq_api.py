import aio_pika
from models.event_rabbitmq import LikeEvent
from fastapi import APIRouter, status

router = APIRouter()


@router.post('/publisher')
async def user_push_publisher(event: LikeEvent) -> None:
    '''
    Publisher добавляет сообщение о событии в RabbitMQ
    Publisher принимает модель Event
    '''
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@notifications-rabbitmq:5672",
    )

    async with connection:

        channel = await connection.channel()
        queue = await channel.declare_queue(event.queue_name)

        await channel.default_exchange.publish(
            aio_pika.Message(body=f"Здравствуйте {event.message_author}!"
                                  f" Ваш комментарий к фильму {event.film_id}"
                                  f" понравился пользователю {event.user_id}".encode()),
            routing_key=queue.name,
        )
        return status.HTTP_200_OK
