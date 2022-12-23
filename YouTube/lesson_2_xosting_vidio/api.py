import shutil
from typing import List
from fastapi import UploadFile , APIRouter , File , Form , Request
from shemas import UploadVidio , GetVidio , User , Massage
from fastapi.responses import JSONResponse

vidio_router = APIRouter()



@vidio_router.post('/',status_code=201)
async def root(title : str =  Form(...) , description : str = Form(...),file :UploadFile = File(...)): # у нас в dsc ожидаем str нов схеме мы ожтдаем int pydantic переобразует int в str но всё равно данные будут не валидные
    info  = UploadVidio(title=title , description=description) #принимаем от пользователя данные и валидируем их
    print(title)
    print(description)
    with open(f'{file.filename}' , 'wb') as buffer:
        shutil.copyfileobj(file.file , buffer)
    return {'file_name ':file.filename , 'info':info}    # мы передали форму и её валидировали


@vidio_router.post('/img')
async def root(files :List[UploadFile] = File(...)):
    for img in files :
        with open(f'{img.filename}' , 'wb') as buffer:
            shutil.copyfileobj(img.file , buffer)
    return {'file_name ':'God'}



@vidio_router.get('/vidio' ,response_model=GetVidio , responses={404 : {'model': Massage}})  #ответ который мы ожидаем
async def get_vidio():
    user = {'id':45,'name':'Rasul' }
    vidio = {'title' : 'Tset' , 'description' : 'dec'}
    info = GetVidio(user=user , vidio=vidio)
    # return info
    return  JSONResponse(status_code=202 , content=info.dict())


@vidio_router.get('/test')  #реквест возвращает все данные который был запрос "с кокого хоста отправили обект реквеста который приходит сервер"
async def test(req:Request):
    print(req.base_url)
    return {}


"""
@vidio_router.get('/vidio')
async def get_vidio():
    user = User(**{'id':45,'name':'Rasul' })
    vidio = UploadVidio(**{'title' : 'Tset' , 'description' : 'dec'})
    return GetVidio(user=user , vidio=vidio)
"""


"""# @vidio_router.post('/info')
# async def info_post(info : UploadVidio):
#     return info
"""


"""# @vidio_router.get('/vidio')
# async def info_get():
#     tit = 'Rasul'
#     desc = 'vidio'
#     return UploadVidio(title=tit , description=desc)"""