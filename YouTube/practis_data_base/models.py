from db import database , metadata
import ormar




class Vidio(ormar.Model):
    class Meta(ormar.ModelMeta):
        database = database
        metadata = metadata

    id : int = ormar.Integer(primary_key=True)
    title : str = ormar.String(max_length=20)
    descriptional : str = ormar.String(max_length=50)
    user : str = ormar.String(max_length=20)

