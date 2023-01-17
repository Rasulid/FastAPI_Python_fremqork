import sys

from fastapi import Depends, HTTPException, status, APIRouter, Request, Form
from sqlalchemy.orm import Session
import models
from DataBase import engine, SessionLocal
from pydantic import BaseModel, Field
from typing import Optional
from .auth import get_current_user, get_user_exception
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from starlette import status
from starlette.responses import RedirectResponse

sys.path.append("..")
router = APIRouter(
    prefix="/todos",
    tags=["ToDos"],
    responses={404: {"description": "Not found"}}
)
models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")  # connect HTML to app with Jinja2


class ToDo(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(lt=6, gt=0, description='The priority must be between 1-5 ')
    complete: bool


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get('/', response_class=HTMLResponse)
async def read_all_by_user(request: Request, db: Session = Depends(get_db)):
    todos = db.query(models.Todos).filter(models.Todos.owner_id == 8).all()

    return templates.TemplateResponse("home.html", {"request": request, "todos": todos})


@router.get("/add-todo", response_class=HTMLResponse)
async def add_new_todo(request: Request):
    return templates.TemplateResponse("add-todo.html", {'request': request})


@router.post("/add-todo", response_class=HTMLResponse)
async def create_todo(request: Request, title: str = Form(...), description: str = Form(...),
                      priority: int = Form(...), db: Session = Depends(get_db)):
    todo_model = models.Todos()
    todo_model.title = title
    todo_model.description = description
    todo_model.priority = priority
    todo_model.complete = False
    todo_model.owner_id = 8

    db.add(todo_model)
    db.commit()

    return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)


@router.get("/edit-todo/{todo_id}", response_class=HTMLResponse)
async def edit_todo(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todos).filter(models.Todos.id == todo_id).first()

    return templates.TemplateResponse("edit-todo.html", {"request": request, "todo": todo})


@router.post("/edit-todo/{todo_id}", response_class=HTMLResponse)
async def create_todo(request: Request, todo_id: int, title: str = Form(...), description: str = Form(...),
                      priority: int = Form(...), db: Session = Depends(get_db)):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    todo_model.title = title
    todo_model.description = description
    todo_model.priority = priority

    db.add(todo_model)
    db.commit()


@router.get('/delete/{todo_id}')
async def delete_todo(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id)\
        .filter(models.Todos.owner_id == 8).first()

    if todo_model is None:
        return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)

    db.query(models.Todos).filter(models.Todos.id == todo_id).delete()

    db.commit()

    return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)


@router.get("/complete/{todo_id}" , response_class=HTMLResponse)
async def complete_todo(request: Request, todo_id: int, db: Session = Depends(get_db)):

    todo = db.query(models.Todos).filter(models.Todos.id == todo_id).first()

    todo.complete = not todo.complete

    db.add(todo)
    db.commit()

    return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)




#
# @router.get('/test') # create request with conected HTML
# async def test(request: Request):
#     return templates.TemplateResponse("login.html", {"request": request})
#
#
# @router.get("/")
# async def read_all(db: Session = Depends(get_db)):
#     return db.query(models.Todos).all()
#
#
# @router.get("/user")
# async def read_all_by_user(user: dict = Depends(get_current_user),
#                            db: Session = Depends(get_db)):
#     if user is None:
#         raise get_user_exception()
#     return db.query(models.Todos) \
#         .filter(models.Todos.owner_id == user.get("id")) \
#         .all()
#
#
# # ______________________________________________
# @router.get("/{todo_id}")
# async def read_todo(todo_id: int,
#                     user: dict = Depends(get_current_user),
#                     db: Session = Depends(get_db)):
#     if user is None:
#         raise get_user_exception()
#     todo_model = db.query(models.Todos) \
#         .filter(models.Todos.id == todo_id) \
#         .filter(models.Todos.owner_id == user.get("id")) \
#         .first()
#     if todo_model is not None:
#         return todo_model
#     raise http_xception()
#
#
#
# # ______________________________________________идентификатор пользователя(post reques)
# @router.post('/')
# async def create_todo(todo: ToDo,
#                       user: dict = Depends(get_current_user),
#                       db: Session = Depends(get_db)):
#     if user is None:
#         raise get_user_exception()
#     models_Todo = models.Todos()
#     models_Todo.title = todo.title
#     models_Todo.description = todo.description
#     models_Todo.priority = todo.priority
#     models_Todo.complete = todo.complete
#     # ______________________________________________идентификатор пользователя(post reques)
#     models_Todo.owner_id = user.get("id")
#
#     db.add(models_Todo)
#     db.commit()
#
#     return {
#         "status": 201,
#         'transaction': 'successfully'
#     }
#
#
# @router.put("/{todo_id}")
# async def update_tod(todo_id: int,
#                      todo: ToDo,
#                      user: dict = Depends(get_current_user),
#                      db: Session = Depends(get_db)):
#     if user is None:
#         raise get_user_exception()
#     todo_model = db.query(models.Todos) \
#         .filter(models.Todos.id == todo_id) \
#         .filter(models.Todos.owner_id == user.get("id")) \
#         .first()
#     # _________________________________________________________________put reques (идентификатор пользователя)
#     if todo_model is None:
#         raise http_xception()
#
#     todo_model.title = todo.title
#     todo_model.description = todo.description
#     todo_model.priority = todo.priority
#     todo_model.complete = todo.complete
#
#     db.add(todo_model)
#     db.commit()
#
#
# # ______________________________________________________delete request
#
# @router.delete('/{todo_id}')
# async def delete_todo(todo_id: int,
#                       user: dict = Depends(get_current_user),
#                       db: Session = Depends(get_db)):
#     if user is None:
#         raise get_user_exception()
#     todo_model = db.query(models.Todos) \
#         .filter(models.Todos.id == todo_id) \
#         .filter(models.Todos.owner_id == user.get("id")) \
#         .delete()
#
#     db.commit()
#     SuccessfulResponses(204)
#     return todo_model
#
#
# # ______________________________________________________delete request
#
# def SuccessfulResponses(status_code: int):
#     return {
#         "status": status_code,
#         'transaction': 'successfully',
#     }
#
#
# def http_xception():
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
