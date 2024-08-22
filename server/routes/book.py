from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status
from server.models.book import UpdateBook
from server.models.book import Book
from server.utils import pydantic_encoder


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_book(book: Book):
    await book.insert()
    return book


@router.get("/", response_model=list[Book])
async def get_books():
    books = await Book.find_all().to_list()
    return books


@router.get("/{id}", response_model=Book)
async def get_book(_id: PydanticObjectId):
    book = await Book.get(_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="not_found"
        )
    return book


@router.put("/{id}", response_model=Book)
async def update_book(_id: PydanticObjectId, book_data: UpdateBook):
    book = await Book.get(_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not found"
        )
    book_data = pydantic_encoder.encode_input(book_data)

    await book.update({"$set": book_data})

    updated_book = await Book.get(_id)
    return updated_book


@router.post('{id}/reviews', response_model=Book)
async def add_review(_id: PydanticObjectId, review: str):
    book = await Book.get(_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not found"
        )
    await book.update({"$push": {"reviews": review}})
    updated_book = await book.get(_id)
    return updated_book


@router.delete("{/id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(_id: PydanticObjectId):
    book = await Book.get(_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not found"
        )
    await book.delete()
    return {"message": "Book deleted successfully"}
