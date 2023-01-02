from sqlalchemy import Boolean, Column, Integer, String
from DataBase import Base


class Todos(Base):
    """
    создания таблицы в SQLalchemy :
        id = int , primery_key = True
        Title = str
        description = str
        priority = int
        complete = Bool , default = False

    """
    __tablename__ = "todos"  #определяем имя таблицы

    id = Column(Integer, primary_key=True , index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)

