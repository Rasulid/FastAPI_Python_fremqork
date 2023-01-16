import sys

from fastapi import Depends, APIRouter
import models
from DataBase import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel
from router.auth import get_current_user, get_user_exception, verify_password, get_password_hash

sys.path.append("..")

router = APIRouter(prefix="/users",
                   tags=["Users"],
                   responses={404: {"description": "User not found"}})
models.Todos.metadata.create_all(bind=engine)


class UserVerification(BaseModel):
    username: str
    password: str
    new_password: str


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("/")
async def get_oll_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@router.get("/user/{user_id}")
async def read_all(user_id: int, db: Session = Depends(get_db)):
    user_model = db.query(models.User).filter(models.User.id == user_id).first()
    if user_model is not None:
        return user_model
    return "invalid user_id"


@router.get('/user/')
async def user_by_query(user_id: int, db: Session = Depends(get_db)):
    query_user_model = db.query(models.User).filter(models.User.id == user_id).first()
    if query_user_model is not None:
        return query_user_model
    return "Invalid user_id"


@router.put("/user/password")
async def user_change_password(user_verification: UserVerification, user: dict = Depends(get_current_user),
                               db: Session = Depends(get_db)):
    print("_____", user)
    if user is None:
        raise get_user_exception()

    user_model = db.query(models.User).filter(models.User.id == user.get("id")).first()

    if user_model is not None:
        if user_verification.username == user_model.username and verify_password(
                user_verification.password,
                user_model.hashed_password):
            user_model.hashed_password == get_password_hash(user_verification.new_password)
            db.add(user_model)
            db.commit()
            return "successful"
    return "invalid user"


@router.delete("/user")
async def delete_user(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()

    user_model = db.query(models.User).filter(models.User.id == user.get("id")).first()

    if user_model is None:
        return "invalid user or request"

    db.query(models.User).filter(models.User.id == user.get("id")).delete()
    db.commit()

    return "commit successes"
#dict = Depends(get_current_user)


@router.delete('/user/test-delete')
async def test_delete(user_id: int, db: Session = Depends(get_db)):
    if user_id is None:
        return "None"
    user_model = db.query(models.User).filter(models.User.id == user_id).delete()

    db.commit()

    return "commit successes"
