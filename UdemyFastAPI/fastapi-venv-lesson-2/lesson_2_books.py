from fastapi import FastAPI

"1 урок мы созали api и отправили словарь с сообшением return {'massage': 'hello bitch!!'} и создали виртуальную среду"
app = FastAPI()


@app.get('/')
async def first_api():
    return {'massage': 'hello bitch!!'}


"2 урок swagger , openapi , request methods & stasus codes"
'docs - обзор'

"""

            operators CRUD
            Create
            Read
            Update
            Delate

get() - Метод чтения : Он извлекает данные 
post() - Создаёт и отправляет данные 
put() - Обновляет ресурс
patch() - обновляет сеть ресурса 
delate() - удаляет ресурс

"""


"""
            не очень используемые операторы 
trace()
options()
connect()
"""

"""
        status code:

1xx - Informational Response - request procesing

2xx - Seccess :Request seccessfuly complate 

3xx - Redirecting: Furter action must be complate 

4xx - Client Error: An error was coused by the request from the client 

5xx - Server Error: An errors was occured on the server 
"""