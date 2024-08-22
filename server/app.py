from fastapi import FastAPI
from server.database import init_db
from server.routes.book import router


app = FastAPI()
app.include_router(router, tags=["Books"], prefix="/books")


@app.on_event("startup")
async def start_db():
    await init_db()


@app.get("/", tags=["Root"])
async def index() -> dict:
    return {"message": "message"}
