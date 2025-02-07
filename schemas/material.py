from pydantic import BaseModel
from models.material import EstadoMaterial
from typing import Optional

# Base para los datos del material, con los campos comunes a las operaciones de creación y actualización
class MaterialBase(BaseModel):
    tipo_material: str  # Tipo de material (ej. libro, herramienta, etc.)
    marca: Optional[str]  # Marca del material (opcional)
    modelo: Optional[str]  # Modelo del material (opcional)
    estado: EstadoMaterial  # Estado del material (Disponible, Prestado, Mantenimiento)

# Modelo para crear un material, heredando de MaterialBase
class MaterialCreate(MaterialBase):
    pass  # No se añaden cambios específicos en este caso

# Modelo para actualizar un material, heredando de MaterialBase
class MaterialUpdate(MaterialBase):
    pass  # No se añaden cambios específicos en este caso

# Modelo de material con ID, para la respuesta y el uso de la base de datos
class Material(MaterialBase):
    id_material: int  # ID único del material

    class Config:
        from_attributes = True  # Permite que los atributos de la base de datos se usen directamente en el modelo
