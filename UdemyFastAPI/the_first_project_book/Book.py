from fastapi import FastAPI
from typing import Optional
app = FastAPI()

BOOKS = {
    'book_1': {'tittle': 'Book one', 'author': 'Author one'},
    'book_2': {'tittle': 'Book one', 'author': 'Author one'},
    'book_3': {'tittle': 'Book one', 'author': 'Author one'},
    'book_4': {'tittle': 'Book one', 'author': 'Author one'},
    'book_5': {'tittle': 'Book one', 'author': 'Author one'}

}


@app.get('/')
async def read_all_books(skip_book: Optional[str] = None):
    if skip_book:
        new_book = BOOKS.copy()
        del new_book[skip_book]
        return new_book
    return BOOKS


@app.get('/{book_name}')
async def read_book(book_name: str):
    return BOOKS[book_name]


@app.post('/')
async def create_book(book_title, book_auther):

    current_book_id = 0

    if len(BOOKS) > 0:
        for book in BOOKS:
            x = int(book.split('_')[-1])
            if x > current_book_id:
                current_book_id = x
            print(x)

    BOOKS[f"book_{current_book_id + 1}"] = {'title': book_title, 'author': book_auther}
    return BOOKS[f'book_{current_book_id + 1}']


@app.put('/{book_name}')
async def update_book(book_name , book_title , book_author):
    book_information = {'title' : book_title , 'author':book_author}
    BOOKS[book_name] = book_information
    return book_information

@app.delete('/{book_name}')
async def delate_book(book_name):
    del BOOKS[book_name]
    return f'book {book_name} was deleted'



@app.get('/assignment/')
async def read_book(book_name):
    return BOOKS[book_name]

@app.delete('/assignment/')
async def delate_book(book_name):
    del BOOKS[book_name]
    return BOOKS