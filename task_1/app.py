from fastapi import FastAPI
from pydantic_model import Message
from publisher import produce_message


app = FastAPI(
    title="Practice with RabbitMQ",
    description="Task_1: send code"
)


@app.post("/send")
def send_code(message: Message):
    return produce_message(message)
