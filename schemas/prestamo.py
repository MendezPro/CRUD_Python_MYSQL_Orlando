from pydantic import BaseModel
from datetime import datetime
from models.prestamo import EstadoPrestamo
from typing import Optional

# Base de datos para el préstamo, con los campos comunes a las operaciones de creación y actualización
class PrestamoBase(BaseModel):
    id_usuario: int  # ID del usuario que realiza el préstamo
    id_material: int  # ID del material que se va a prestar
    fecha_prestamo: datetime  # Fecha en la que se realiza el préstamo
    fecha_devolucion: Optional[datetime]  # Fecha opcional de devolución del material
    estado: EstadoPrestamo  # Estado del préstamo (Activo, Devuelto, Vencido)

# Modelo para crear un préstamo, heredando de PrestamoBase
class PrestamoCreate(PrestamoBase):
    pass  # No se añaden cambios específicos en este caso

# Modelo para actualizar un préstamo, heredando de PrestamoBase
class PrestamoUpdate(PrestamoBase):
    pass  # No se añaden cambios específicos en este caso

# Modelo de préstamo con ID, para la respuesta y el uso de la base de datos
class Prestamo(PrestamoBase):
    id_prestamo: int  # ID único del préstamo

    class Config:
        from_attributes = True  # Permite que los atributos de la base de datos se usen directamente en el modelo
