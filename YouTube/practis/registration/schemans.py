from pydantic import BaseModel
from typing import List

class UserRegister(BaseModel):
    name : str
    surname : str
    age : int
    id : int
    facultet : str

