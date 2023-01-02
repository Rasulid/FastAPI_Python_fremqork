from fastapi import FastAPI
import models
from DataBase import engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


@app.get('/')
async def create_data_base():
    return {"database": "Created"}
