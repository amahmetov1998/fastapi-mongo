import pika
from config import settings

connection_params = pika.ConnectionParameters(host=settings.RMQ_HOST,
                                              port=settings.RMQ_PORT,
                                              credentials=pika.PlainCredentials(username=settings.RMQ_USER,
                                                                                password=settings.RMQ_PASSWORD)
                                              )


def get_connection() -> pika.BlockingConnection:
    return pika.BlockingConnection(parameters=connection_params)
