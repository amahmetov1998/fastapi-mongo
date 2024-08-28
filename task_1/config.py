import logging
from pydantic import BaseModel
from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv
import sys

sys.path.insert(0, '..')


class RunConfig(BaseModel):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class Settings(BaseSettings):
    RMQ_USER: str = os.getenv("RMQ_USER", "guest")
    RMQ_HOST: str = os.getenv("RMQ_HOST", "127.0.0.1")
    RMQ_PORT: int = os.getenv("RMQ_PORT", 5672)
    RMQ_PASSWORD: str = os.getenv("RMQ_PASSWORD", "guest")
    RMQ_EXCHANGE: str = os.getenv("RMQ_EXCHANGE", "new_exchange")
    RMQ_ROUTING_KEY: str = os.getenv("RMQ_ROUTING_KEY", "key")
    EMAIL_QUEUE: str = os.getenv("EMAIL_QUEUE", "email")
    PHONE_QUEUE: str = os.getenv("PHONE_QUEUE", "phone")
    TELEGRAM_QUEUE: str = os.getenv("TELEGRAM_QUEUE", "telegram")

    run: RunConfig = RunConfig()


load_dotenv()
settings = Settings()


logger = logging.getLogger('rabbitmq_task_1')
logger.setLevel(logging.INFO)
stream_output = logging.StreamHandler(stream=sys.stdout)
file_logging_handler = logging.FileHandler(filename="log.txt")
file_logging_handler.setFormatter(logging.Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
logger.addHandler(stream_output)
logger.addHandler(file_logging_handler)
