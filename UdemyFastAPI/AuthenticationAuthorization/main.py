from fastapi import FastAPI, Depends , HTTPException
import models
from DataBase import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel , Field
from typing import Optional

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class ToDo(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(gt=0, lt=6, description='The priority must be between 1-5 ')
    complete: bool
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get('/')
async def read_all(db: Session = Depends(get_db)):
    return db.query(models.Todos).all()


@app.get('/{todo_id}')
async def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise http_xception()


@app.post('/')
async def create_todo(todo:ToDo , db:Session = Depends(get_db)):
    models_Todo = models.Todos()
    models_Todo.title = todo.title
    models_Todo.description = todo.description
    models_Todo.priority = todo.priority
    models_Todo.complete = todo.complete

    db.add(models_Todo)
    db.commit()

    return {
        'status': 201,
        'transaction': 'successfully'
    }


@app.put('/{todo_id}')
async def update_todo(todo_id: int, todo: ToDo, db: Session = Depends(get_db)):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()

    if todo_model is None:
        raise http_xception()

    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete

    db.add(todo_model)
    db.commit()


@app.delete('/{delete_todo}')
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).delete()

    db.commit()
    SuccessfulResponses(204)
    return todo_model


def SuccessfulResponses(status_code:int):
    return {
        "status":status_code,
        'transaction': 'successfully',
    }

def http_xception():
    raise HTTPException(status_code=404, detail="Todo not found")
