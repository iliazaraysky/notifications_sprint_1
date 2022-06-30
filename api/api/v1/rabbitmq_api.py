import aio_pika
from models.event_rabbitmq import Event
from fastapi import APIRouter, status

router = APIRouter()


@router.post('/publisher')
async def publisher(event: Event) -> None:
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
            aio_pika.Message(body=f"Hello {event.body}".encode()),
            routing_key=queue.name,
        )
        return status.HTTP_200_OK
