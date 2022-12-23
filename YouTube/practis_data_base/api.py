from fastapi import APIRouter , File , UploadFile
from models import Vidio
from  schemas import Vidio_info , Massage
import shutil


api_router = APIRouter()

@api_router.get('/')
def root():
    return {'messege': 'hello bitch'}

@api_router.post('/vidio')
async def widio(title : str = File(...), disc : str = File(...)):
    info = Vidio_info(title=title, discription=disc)
    return { 'info':info}


@api_router.post('/vidos')
async def root(vidio : Vidio):
    await vidio.save()
    return vidio

@api_router.get('/vidio/{users_id}' ,response_model=Vidio_info , responses={404 : {'model': Massage}})  #ответ который мы ожидаем
async def get_vidio(users_id:int):
    # user = User
    return await Vidio.objects.select_related('user').get(pk=users_id)