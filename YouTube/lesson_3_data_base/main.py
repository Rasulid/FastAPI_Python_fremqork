from db import database , metadata ,engin
from fastapi import FastAPI
from api import vidio_router

app = FastAPI()


metadata.create_all(engin)  #sqlite файл появляется
app.state.database = database   # в стате добавляем метод дата бейз , при запросах будет доступен конект с базой данных


@app.on_event("startup") #запускается ассинхроная функцыя
async def startup() -> None:
    database_ = app.state.database  # создаём локальную переменную
    if not database_.is_connected:  # Если у нас нету конекта
        await database_.connect()   # мы делаем конект базе


@app.on_event("shutdown")  # то же самое, Если конект есть мы выключаемся
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()

app.include_router(vidio_router)

