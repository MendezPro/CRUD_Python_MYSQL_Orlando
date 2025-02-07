import models.prestamo
import schemas.prestamo
from sqlalchemy.orm import Session

# Función para obtener todos los préstamos, con paginación
def get_prestamos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.prestamo.Prestamo).offset(skip).limit(limit).all()

# Función para obtener un solo préstamo por su ID
def get_prestamo(db: Session, id: int):
    return db.query(models.prestamo.Prestamo).filter(models.prestamo.Prestamo.id_prestamo == id).first()

# Función para crear un nuevo préstamo en la base de datos
def create_prestamo(db: Session, prestamo: schemas.prestamo.PrestamoCreate):
    db_prestamo = models.prestamo.Prestamo(**prestamo.dict())  # Crear un objeto Prestamo a partir del schema
    db.add(db_prestamo)  # Agregar el nuevo préstamo a la sesión
    db.commit()  # Confirmar cambios en la base de datos
    db.refresh(db_prestamo)  # Actualizar el objeto db_prestamo con los datos de la base
    return db_prestamo

# Función para actualizar un préstamo existente por su ID
def update_prestamo(db: Session, prestamo: schemas.prestamo.PrestamoUpdate, id: int):
    db_prestamo = db.query(models.prestamo.Prestamo).filter(models.prestamo.Prestamo.id_prestamo == id).first()  # Buscar préstamo por ID
    if db_prestamo:
        # Actualizar cada campo del préstamo si el valor no es None
        for key, value in prestamo.dict(exclude_unset=True).items():
            setattr(db_prestamo, key, value)
        db.commit()  # Confirmar cambios
        db.refresh(db_prestamo)  # Actualizar el objeto db_prestamo con los datos de la base
    return db_prestamo

# Función para eliminar un préstamo por su ID
def delete_prestamo(db: Session, id: int):
    db_prestamo = db.query(models.prestamo.Prestamo).filter(models.prestamo.Prestamo.id_prestamo == id).first()  # Buscar préstamo por ID
    if db_prestamo:
        db.delete(db_prestamo)  # Eliminar el préstamo de la base de datos
        db.commit()  # Confirmar cambios
    return db_prestamo
