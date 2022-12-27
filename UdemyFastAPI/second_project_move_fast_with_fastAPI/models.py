from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from veribels import BOOKS


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(max_length=100, min_length=1)
    description: Optional[str] = Field(title='the description on Book',
                                       min_length=1,
                                       max_length=100)
    rating: int = Field(gt=-1, lt=101)

    class Config:
        schema_extra = {
            "example": dict(id='035fd52b-ff43-4685-bdb7-501193dcc64e', title='book name', author='name author',
                            description='the book description', rating=69)
        }


def create_book_without_ip():
    book_1 = Book(id="135fd52b-ff43-4685-bdb7-501193dcc64e",
                  title='title 1',
                  author='author 1',
                  description='Description 1',
                  rating=50)

    book_2 = Book(id="235fd52b-ff43-4685-bdb7-501193dcc64e",
                  title='title 2',
                  author='author 2',
                  description='Description 2',
                  rating=60)

    book_3 = Book(id="335fd52b-ff43-4685-bdb7-501193dcc64e",
                  title='title 3',
                  author='author 3',
                  description='Description 3',
                  rating=70)

    book_4 = Book(id="435fd52b-ff43-4685-bdb7-501193dcc64e",
                  title='title 4',
                  author='author 4',
                  description='Description 4',
                  rating=80)

    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)
