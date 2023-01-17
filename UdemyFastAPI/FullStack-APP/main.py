from fastapi import FastAPI, Depends
import models
from DataBase import engine
from router import auth, todos, address
from starlette.staticfiles import StaticFiles


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static") #connect CSS with starlete

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(address.router)


