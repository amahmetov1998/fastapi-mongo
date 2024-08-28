from config import settings
from pydantic_model import Message
from rabbit import get_connection


def produce_message(message: Message) -> None:
    try:
        with get_connection() as connection:
            with connection.channel() as channel:

                channel.exchange_declare(exchange=settings.RMQ_EXCHANGE, exchange_type='direct')

                queues = [
                    settings.EMAIL_QUEUE, settings.PHONE_QUEUE, settings.TELEGRAM_QUEUE
                ]
                for queue in queues:
                    channel.queue_declare(queue=queue)
                    channel.queue_bind(exchange=settings.RMQ_EXCHANGE,
                                       routing_key=settings.RMQ_ROUTING_KEY,
                                       queue=queue)

                channel.basic_publish(
                    exchange=settings.RMQ_EXCHANGE,
                    routing_key=settings.RMQ_ROUTING_KEY,
                    body=message.json()
                )
    except KeyboardInterrupt:
        pass
