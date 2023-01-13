from fastapi import FastAPI, Depends, HTTPException
import models
from DataBase import engine, SessionLocal
from sqlalchemy.orm import Session


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


@app.get('/')
async def read_all(db: Session = Depends(get_db)):
    return db.query(models.Books).all()
