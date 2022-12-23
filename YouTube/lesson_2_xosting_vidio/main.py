from fastapi import FastAPI
from api import vidio_router

app = FastAPI()
app.include_router(vidio_router)

