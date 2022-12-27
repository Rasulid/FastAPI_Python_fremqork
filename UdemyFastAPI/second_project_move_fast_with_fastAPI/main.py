from fastapi import FastAPI
from typing import Optional
from models import Book, create_book_without_ip
from veribels import BOOKS
from uuid import UUID

app = FastAPI()


@app.get('/')
async def read_all_books(books_to_return: Optional[int] = None):
    if len(BOOKS) < 1:
        create_book_without_ip()

    if books_to_return and len(BOOKS) >= books_to_return > 0:
        i = 1
        new_books = []
        while i <= books_to_return:
            new_books.append(BOOKS[i - 1])
            i += 1
        return new_books
    return BOOKS


@app.post('/')
async def create_book(book: Book):
    BOOKS.append(book)
    return book


@app.get('/book/{book_id}')
async def book_id(book_ids: UUID):
    for x in BOOKS:
        if x.id == book_ids:
            return x


@app.put('/{book_id}')
async def update_book(books_id: UUID, book: Book):
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == books_id:
            BOOKS[counter - 1] = book
            return BOOKS[counter - 1]


@app.delete('/{book_id}')
async def delete_book(book_ides: UUID):
    count = 0

    for x in BOOKS:
        count += 1
        if x.id == book_ides:
            del BOOKS[count - 1]
            return f'id {book_ides} was delete'
