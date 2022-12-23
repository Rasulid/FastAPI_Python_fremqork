import shutil

from typing import List
from pathlib import Path
from fastapi import UploadFile , APIRouter , File , Form , BackgroundTasks , HTTPException
from schemas import UploadVidio , GetVidio
from models import Vidio , User
from services import write_vidio


vidio_router = APIRouter()


@vidio_router.post('/',status_code=201)
async def creat_vidio(
        background_tasks : BackgroundTasks,
        tittle : str =  Form(...) ,
        description : str = Form(...),
        file_1 :UploadFile = File(...)
): # у нас в dsc ожидаем str нов схеме мы ожтдаем int pydantic переобразует int в str но всё равно данные будут не валидные
    file_type= f"media/{file_1.filename}"
    print('FILE CONTENT TYPE --------------------' , file_1.content_type)
    if file_1.content_type == 'video/mp4':
        print('FILE CONTENT TYPE --------------------' , file_1.content_type)
        background_tasks.add_task(write_vidio , file_type ,file_1) # background_tasks - мы не будем дожидаться своего ответа , мы дадим команду и она сама выполняется /
        with open(f'{file_1.filename}', 'wb') as buffer:
            shutil.copyfileobj(file_1.file, buffer)
    else :
        raise HTTPException(status_code=418 , detail="it isn't mp4")
    info  = UploadVidio(tittle=tittle , description=description) #принимаем от пользователя данные и валидируем их
    user = await User.objects.first()
    print(30,user)
    print('ssssssss------------s')
    return await Vidio.objects.create(file=file_1.filename ,user = user, **info.dict())
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
