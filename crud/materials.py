import models.material
import schemas.material
from sqlalchemy.orm import Session

# Función para obtener todos los materiales, con paginación
def get_materials(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.material.Material).offset(skip).limit(limit).all()

# Función para obtener un solo material por su ID
def get_material(db: Session, id: int):
    return db.query(models.material.Material).filter(models.material.Material.id_material == id).first()

# Función para crear un nuevo material en la base de datos
def create_material(db: Session, material: schemas.material.MaterialCreate):
    db_material = models.material.Material(**material.dict())  # Crear un objeto Material a partir del schema
    db.add(db_material)  # Agregar el nuevo material a la sesión
    db.commit()  # Confirmar cambios en la base de datos
    db.refresh(db_material)  # Actualizar el objeto db_material con los datos de la base
    return db_material

# Función para actualizar un material existente por su ID
def update_material(db: Session, material: schemas.material.MaterialUpdate, id: int):
    db_material = db.query(models.material.Material).filter(models.material.Material.id_material == id).first()  # Buscar material por ID
    if db_material:
        # Actualizar cada campo del material si el valor no es None
        for key, value in material.dict(exclude_unset=True).items():
            setattr(db_material, key, value)
        db.commit()  # Confirmar cambios
        db.refresh(db_material)  # Actualizar el objeto db_material con los datos de la base
    return db_material

# Función para eliminar un material por su ID
def delete_material(db: Session, id: int):
    db_material = db.query(models.material.Material).filter(models.material.Material.id_material == id).first()  # Buscar material por ID
    if db_material:
        db.delete(db_material)  # Eliminar el material de la base de datos
        db.commit()  # Confirmar cambios
    return db_material
