from pydantic_model import EmailResponse, PhoneResponse
from exceptions import TelegramError, PhoneError
import random
from config import logger


def email_callback(ch, method, properties, body: bytes):
    data = EmailResponse.parse_raw(body)
    logger.info(f"Я отправил на почту {data.email} код {data.code}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def phone_callback(ch, method, properties, body: bytes):
    data = PhoneResponse.parse_raw(body)
    if random.choice([True, False]):
        logger.info(f"Я отправил на телефон {data.phone} код {data.code}")
    else:
        raise PhoneError("Сообщение не отправлено")

    ch.basic_ack(delivery_tag=method.delivery_tag)


def telegram_callback(ch, method, properties, body: bytes):
    ch.basic_ack(delivery_tag=method.delivery_tag)
    raise TelegramError("Сообщение не отправлено")
