import uvicorn
import asyncio
import aio_pika
from models.event import Event
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse


app = FastAPI(
    title='Notifications API',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


@app.get('/publisher')
async def publisher() -> None:
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@notifications-rabbitmq:5672",
    )

    async with connection:
        routing_key = "test_queue"

        channel = await connection.channel()
        queue = await channel.declare_queue("hello")

        await channel.default_exchange.publish(
            aio_pika.Message(body=f"Hello {routing_key}".encode()),
            routing_key=queue.name,
        )


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8001)