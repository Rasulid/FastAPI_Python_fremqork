from pydantic import BaseModel
from  fastapi import  UploadFile


class Vidio_info(BaseModel):
    title : str
    description : str = None
    user : str = 'hi'


class Massage(BaseModel):
    massage : str