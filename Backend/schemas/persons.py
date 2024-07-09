from typing import List, Union
from pydantic  import BaseModel
from datetime import datetime,date

class PersonBase(BaseModel):
    Titulo_Cortesia:str
    Nombre:str
    Primer_Apellido:str
    Segundo_Apellido:str
    Foto:str
    Genero:str
    Tipo_Sangre:str
    Estatus: bool
    Fecha_Nacimiento:date
    Fecha_Actualizacion:datetime
    # Id_persona: int

class PersonCreate(PersonBase):
    pass

class PersonUpdate(PersonBase):
    pass

class Person(PersonBase):
    ID:int
    # owner_id: int clave foranea
    class Config:
        orm_mode = True
        