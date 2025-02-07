from sqlalchemy import Column, Integer, String, DateTime, Enum
from config.db import Base
import enum

class TipoUsuario(str, enum.Enum):
    Alumno = "Alumno"
    Profesor = "Profesor"
    Secretaria = "Secretaria"
    Laboratorista = "Laboratorista"
    Directivo = "Directivo"
    Administrativo = "Administrativo"

class Status(str, enum.Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"
    Bloqueado = "Bloqueado"
    Suspendido = "Suspendido"


class User(Base):
    __tablename__ = "tbb_usuario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(60))
    primerApellido = Column(String(60))
    segundoApellido = Column(String(60))
    tipoUsuario = Column(Enum(TipoUsuario))
    nombreUsuario = Column(String(60), unique=True, index=True)
    correoElectronico = Column(String(100), unique=True, index=True)
    contrasena = Column(String(100))
    nombreTelefono = Column(String(20))
    status = Column(Enum(Status))
    fechaRegistro = Column(DateTime)
    fechaActualizacion = Column(DateTime)

   