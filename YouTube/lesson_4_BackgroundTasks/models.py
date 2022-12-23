from db import metadata, database
from fastapi import UploadFile
from typing import Optional, Union, Dict
import ormar
import datetime


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class User(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    username: str = ormar.String(max_length=50)


class Vidio(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    tittle: str = ormar.String(max_length=50)
    description: str = ormar.String(max_length=500)
    file: str = ormar.String(max_length=1000)
    create_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    # user: Optional[User] = ormar.ForeignKey(User)  # сылает в класс User
    user: Optional[Union[User, Dict]] = ormar.ForeignKey(User)
