from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum
from config.db import Base
import enum

# Definimos un enum para los posibles estados del préstamo
class EstadoPrestamo(str, enum.Enum):
    Activo = "Activo"  # El préstamo está activo
    Devuelto = "Devuelto"  # El préstamo ha sido devuelto
    Vencido = "Vencido"  # El préstamo ha vencido

# Definimos el modelo de la tabla "tbb_prestamo"
class Prestamo(Base):
    __tablename__ = "tbb_prestamo"  # Nombre de la tabla en la base de datos

    # Definición de las columnas en la tabla
    id_prestamo = Column(Integer, primary_key=True, autoincrement=True)  # ID del préstamo, clave primaria
    id_usuario = Column(Integer, ForeignKey('tbb_usuario.id'), nullable=False)  # ID del usuario relacionado, clave foránea
    id_material = Column(Integer, ForeignKey('tbb_material.id_material'), nullable=False)  # ID del material relacionado, clave foránea
    fecha_prestamo = Column(DateTime, nullable=False)  # Fecha en la que se realiza el préstamo
    fecha_devolucion = Column(DateTime, nullable=True)  # Fecha en la que se devuelve el material (puede ser nula)
    estado = Column(Enum(EstadoPrestamo), nullable=False)  # Estado del préstamo (Activo, Devuelto o Vencido)
