import asyncio
import logging

import aio_pika
from aio_pika.abc import AbstractIncomingMessage


async def on_message(message: AbstractIncomingMessage) -> None:
    print(" [x] Received message %r" % message)
    print("Message body is: %r" % message.body)
    await asyncio.sleep(5)


async def main(queue_name: str) -> None:
    connection = await aio_pika.connect(
        "amqp://guest:guest@localhost/",
    )
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue(queue_name)
        await queue.consume(on_message, no_ack=True)

        print(" [*] Waiting for messages. To exit press CTRL+C")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main('test_queue'))
