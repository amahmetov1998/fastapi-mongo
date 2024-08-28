import uvicorn
from config import settings


if __name__ == "__main__":
    uvicorn.run("app:app",
                host=settings.run.HOST,
                port=settings.run.PORT,
                reload=True)
