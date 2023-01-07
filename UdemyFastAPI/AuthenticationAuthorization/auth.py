from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
import models
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from DataBase import SessionLocal, engine
from fastapi.security import OAuth2PasswordRequestForm


class CreateUser(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
models.Base.metadata.create_all(bind=engine)  # это создаёт нашу базу данных и сделает всё необходимое для таблици
app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_password_hash(password):  # хеширует пароль
    return bcrypt_context.hash(password)


def verify_password(plain_password,
                    hashed_password):  # проверяем порольпользователя , сравниваем хешированный пароль с обычным
    return bcrypt_context.verify(plain_password, hashed_password)


def authenticate_user(user: str, password: str,
                      db):  # Авторизацыи пользователя , Это функция проверяет пароль и username
    user = db.query(models.User) \
        .filter(models.User.username == user) \
        .first()

    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


@app.post('/create/user')
async def create_new_user(create_user: CreateUser, db: Session = Depends(get_db)):
    create_user_model = models.User()
    create_user_model.email = create_user.email
    create_user_model.name = create_user.first_name
    create_user_model.surname = create_user.last_name

    hash_password = get_password_hash(create_user.password)

    create_user_model.hashed_password = hash_password
    create_user_model.username = create_user.username
    create_user_model.is_active = True

    db.add(create_user_model)
    db.commit()


@app.post('/token')
async def login_for_access_token(from_data: OAuth2PasswordRequestForm = Depends()
                                 , db: Session = Depends(get_db)):
    user = authenticate_user(from_data.username, from_data.password, db)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return 'User is Validated'
