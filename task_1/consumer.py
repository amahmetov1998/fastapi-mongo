from config import settings
from rabbit import get_connection
from callback import email_callback, telegram_callback, phone_callback


def consume_messages() -> None:
    with get_connection() as connection:
        with connection.channel() as channel:

            channel.basic_consume(queue=settings.EMAIL_QUEUE, on_message_callback=email_callback)
            channel.basic_consume(queue=settings.PHONE_QUEUE, on_message_callback=phone_callback)
            channel.basic_consume(queue=settings.TELEGRAM_QUEUE, on_message_callback=telegram_callback)

            channel.start_consuming()


if __name__ == "__main__":
    consume_messages()
