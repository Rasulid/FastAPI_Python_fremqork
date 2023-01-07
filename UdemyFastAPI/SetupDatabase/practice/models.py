from DataBase import Base
from sqlalchemy import Integer , String , Column , Boolean

class Books(Base):
    __tablename__ = "books"

    id = Column(Integer , primary_key=True , index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(String)
    complete = Column(Boolean , default=False)