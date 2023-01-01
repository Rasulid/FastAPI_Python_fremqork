from fastapi import FastAPI, HTTPException, Request , status ,Form , Header
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse


class NegativeNumberExceptions(Exception):
    def __init__(self, books_to_return):
        self.books_to_return = books_to_return


app = FastAPI()

BOOKS = []


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

class BookNoReting(BaseModel):
    id: UUID
    title :str = Field(min_length=1)
    author:str
    description : Optional[str] = Field(None , title='Description of the book',
                                        max_length=100 ,
                                        min_length=1)
@app.exception_handler(NegativeNumberExceptions)

async def negative_number(request: Request,
                          exceptions: NegativeNumberExceptions):
    return JSONResponse(status_code=418,
                        content = {'message': f"hey why do you want {exceptions.books_to_return} books you need read "
                                              f"more !"}
                        )



#_________________________________________________Assignment------------------------------------------------------------------

@app.post('/books/login')
async def book_login(book_id : int,username:Optional[ str] = Header(None), password: Optional[ str] = Header(None)):


    if username == "FastAPIUser" and password == "test1234!":
        return BOOKS[book_id]
    raise HTTPException(status_code=404 , headers={"Message": 'Invalid User'})
#_________________________________________________Assignment------------------------------------------------------------------



@app.get('/heder')
async def read_header(random_header: Optional[str] = Header(None)):
    return {'random-header':random_header}



@app.get('/')
async def read_all_books(books_to_return: Optional[int] = None):
    if books_to_return and books_to_return < 0:
        raise NegativeNumberExceptions(books_to_return=books_to_return)

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


@app.get('/book/rating/{book_id}' , response_model=BookNoReting)
async def read_book_no_rating(book_ids: UUID):
    for x in BOOKS:
        if x.id == book_ids:
            return x
    raise raise_item_not_founded()

@app.post('/' , status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    BOOKS.append(book)
    return book


@app.get('/book/{book_id}')
async def book_id(book_ids: UUID):
    for x in BOOKS:
        if x.id == book_ids:
            return x
    raise raise_item_not_founded()


@app.put('/{book_id}')
async def update_book(books_id: UUID, book: Book):
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == books_id:
            BOOKS[counter - 1] = book
            return BOOKS[counter - 1]
    raise raise_item_not_founded()


@app.delete('/{book_id}')
async def delete_book(book_ides: UUID):
    count = 0

    for x in BOOKS:
        count += 1
        if x.id == book_ides:
            del BOOKS[count - 1]
            return f'id {book_ides} was delete'

    raise raise_item_not_founded()


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


def raise_item_not_founded():
    return HTTPException(status_code=404, detail="Book is not defined",
                         headers={'X-Header-Error': "Not found the book UUID"})

