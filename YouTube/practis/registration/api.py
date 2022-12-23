from fastapi import APIRouter , File , Request , UploadFile
from schemans import UserRegister
from typing import List
import shutil

api_router = APIRouter()




@api_router.get('/request')
async def request(req : Request):
    print(req.base_url)
    return {}


# @vidio_router.post('/img')
# async def root(files :List[UploadFile] = File(...)):
#     for img in files :
#         with open(f'{img.filename}' , 'wb') as buffer:
#             shutil.copyfileobj(img.file , buffer)
#     return {'file_name ':'God'}

@api_router.post('/')
async def register(files : List[UploadFile] = File(...)):
    for img in files:
        with open(f'{img.filename}', 'wb') as file:
            shutil.copyfileobj(img.file, file)
    return {'filename': 'good'}


@api_router.post('/register' , response_model=UserRegister)
async def register( name : str = File(... , max_length= 25 , min_length=1 , ), surname : str = File(... ,max_length= 25 , min_length=1),age : int = File(... ),id : int = File(... ), facultet : str = File(...,max_length= 25 , min_length=1) ):
    return UserRegister(name=name, surname=surname, age=age, id=id, facultet=facultet)