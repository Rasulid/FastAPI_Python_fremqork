from typing import List
from pydantic import BaseModel


class User(BaseModel):         #здесь мы будем проинимать данные от сервера
    id : int
    name : str

class UploadVidio(BaseModel):      #здесь мы будем проинимать данные от сервера
    title : str
    description : str
    # tags : List[str] = None

# а здесь мы будем сериолизовать и обработаь эти даные
class GetVidio(BaseModel):        #мы создали pydantic модель которое для наших свойств используется pydantic дадели
    user : User
    vidio : UploadVidio


class Massage(BaseModel):
    massage : str