from sqlalchemy import Column, Integer, String, Enum
from config.db import Base
import enum

# Enum que define los estados posibles para el material
class EstadoMaterial(str, enum.Enum):
    Disponible = "Disponible"
    Prestado = "Prestado"
    Mantenimiento = "En Mantenimiento"

# Modelo de la tabla "tbb_material" que representa el material en la base de datos
class Material(Base):
    __tablename__ = "tbb_material"  # Definimos el nombre de la tabla en la base de datos

    id_material = Column(Integer, primary_key=True, autoincrement=True)  # Clave primaria para el material
    tipo_material = Column(String(100), nullable=False)  # Tipo de material, no puede ser nulo
    marca = Column(String(100), nullable=True)  # Marca del material (opcional)
    modelo = Column(String(100), nullable=True)  # Modelo del material (opcional)
    estado = Column(Enum(EstadoMaterial), nullable=False)  # Estado del material (Enum: Disponible, Prestado, Mantenimiento)
