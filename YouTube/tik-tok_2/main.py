import shutil
from typing import List
from fastapi import FastAPI , UploadFile , File

app = FastAPI()

@app.post('/')
async def root(file : UploadFile = File(...)):
    with open(f'{file.filename}' , 'wb') as vid :
        shutil.copyfileobj(file.file , vid)
    return {"file" : file.filename}

@app.post('/img')
async def root(file : list[UploadFile] = File(...)):
    for img in file:
        with open(f'{img.filename}' , 'wb') as vid :
            shutil.copyfileobj(img.file , vid)
    return {"file" :'good'}
