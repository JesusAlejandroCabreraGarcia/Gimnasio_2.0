from sqlalchemy import Column,Boolean, Integer, String, DateTime, ForeignKey,Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import models.persons
import enum

class MyEstatus(enum.Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"
    Bloqueado = "Bloqueado"
    Suspendido = "Suspendidos"

class User(Base):
    __tablename__ = 'tbb_usuarios'

    ID = Column(Integer, primary_key=True, index=True)
    Persona_ID = Column(Integer, ForeignKey("tbb_personas.ID"))
    Nombre_Usuario = Column(String(100))
    Correo_Electronico = Column(String(100))
    Contrasena = Column(String(100))
    Numero_Telefono_Movil = Column(String(100))
    Estatus = Column('value', Enum(MyEstatus))
    Fecha_Registro = Column(DateTime())
    Fecha_Actualizacion= Column(DateTime())
    # intems = relationship("Item", back_populates="owner") Clave foranea