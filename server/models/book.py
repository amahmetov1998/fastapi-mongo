from beanie import Document
from pydantic import BaseModel
from typing import Optional


class Review:
    review: str


class Book(Document):
    title: str
    author: str
    published_year: int
    reviews: list[str] = []

    class Settings:
        name = "books_collection"

    class Config:
        json_schema_extra = {"example": {"title": "name",
                                         "author": "name",
                                         "published_year": "year",
                                         "review": "review"
                                         }
                             }


class UpdateBook(BaseModel):
    title: Optional[str]
    author: Optional[str]
    published_year: Optional[int]
