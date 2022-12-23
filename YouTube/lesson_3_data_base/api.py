import shutil
from typing import List
from fastapi import UploadFile , APIRouter , File , Form
from schemas import UploadVidio , GetVidio
from models import Vidio , User

vidio_router = APIRouter()


@vidio_router.post('/',status_code=201)
async def creat_vidio(tittle : str =  Form(...) , description : str = Form(...),file :UploadFile = File(...)): # у нас в dsc ожидаем str нов схеме мы ожтдаем int pydantic переобразует int в str но всё равно данные будут не валидные

    info  = UploadVidio(tittle=tittle , description=description) #принимаем от пользователя данные и валидируем их
    with open(f'{file.filename}' , 'wb') as buffer:
        shutil.copyfileobj(file.file , buffer)
    user = await User.objects.first()
    return await Vidio.objects.create(file=file.filename ,user = user, **info.dict())
    # return {'file_name ':file.filename , 'info':info}    # мы передали форму и её валидировали





@vidio_router.get('/vidio/{users_id}' ,response_model=GetVidio )  #ответ который мы ожидаем
async def get_vidio(users_id:int):
    query =await Vidio.objects.select_related('user').get(pk=users_id)
    print("QUERY ----------", query)
    return query
    # return await Vidio.objects.select_related('user').get(pk=users_id)



 # query =await Vidio.objects.select_related('user').get(pk=users_id)
 #    print("QUERY ----------", query)
 #    return query





"""

@vidio_router.post('/img')
async def root(files :List[UploadFile] = File(...)):
    for img in files :
        with open(f'{img.filename}' , 'wb') as buffer:
            shutil.copyfileobj(img.file , buffer)
    return {'file_name ':'God'}


@vidio_router.post('/vidio')
async def creat_vidio(vidio:Vidio):
    await vidio.save()
    return vidio





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


@vidio_router.get('/vidio')
async def get_vidio():
    user = User(**{'id':45,'name':'Rasul' })
    vidio = UploadVidio(**{'title' : 'Tset' , 'description' : 'dec'})
    return GetVidio(user=user , vidio=vidio)



@vidio_router.post('/info')
async def info_post(info : UploadVidio):
    return info



@vidio_router.get('/vidio')
async def info_get():
    tit = 'Rasul'
    desc = 'vidio'
    return UploadVidio(title=tit , description=desc)"""