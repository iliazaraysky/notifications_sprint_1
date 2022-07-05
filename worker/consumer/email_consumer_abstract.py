from abc import ABC


class ConsumeEmailAbstract(ABC):
    """
    Консумер забирает сообщения из очереди RabbitMQ
    """

    def decoder(self, body):
        pass

    def message(self, channel, deliver, body):
        pass

