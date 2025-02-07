import models.user
import schemas.users
from sqlalchemy.orm import Session
from datetime import datetime

# Función para obtener todos los usuarios, con paginación
def get_users(db: Session, skip: int = 0, limit: int = 0):
    return db.query(models.user.User).offset(skip).limit(limit).all()

# Función para obtener un solo usuario por su ID
def get_user(db: Session, id: int):
    return db.query(models.user.User).filter(models.user.User.id == id).first()

# Función para obtener un usuario por su nombre de usuario
def get_user_by_usuario(db: Session, nombreUsuario: str):
    return db.query(models.user.User).filter(models.user.User.nombreUsuario == nombreUsuario).first()

# Función para crear un nuevo usuario en la base de datos
def create_user(db: Session, user: schemas.users.UserCreate):
    db_user = models.user.User(
        nombre=user.nombre,
        primerApellido=user.primerApellido,
        segundoApellido=user.segundoApellido,
        tipoUsuario=user.tipoUsuario,
        nombreUsuario=user.nombreUsuario,
        correoElectronico=user.correoElectronico,
        contrasena=user.contrasena,
        nombreTelefono=user.nombreTelefono,
        status=user.status,
        fechaRegistro=datetime.utcnow(),  # Fecha de registro
        fechaActualizacion=datetime.utcnow()  # Fecha de la última actualización
    )
    db.add(db_user)  # Agregar el nuevo usuario a la sesión
    db.commit()  # Confirmar cambios en la base de datos
    db.refresh(db_user)  # Actualizar el objeto db_user con los datos de la base
    return db_user

# Función para actualizar los datos de un usuario existente
def update_user(db: Session, id: int, user: schemas.users.UserUpdate):
    db_user = db.query(models.user.User).filter(models.user.User.id == id).first()  # Buscar usuario por ID
    if db_user:
        # Actualizar cada campo del usuario si el valor es diferente de None
        for var, value in vars(user).items():
            setattr(db_user, var, value) if value else None
    db.commit()  # Confirmar cambios
    db.refresh(db_user)  # Actualizar el objeto db_user con los datos de la base
    return db_user

# Función para eliminar un usuario por su ID
def delete_user(db: Session, id: int):
    db_user = db.query(models.user.User).filter(models.user.User.id == id).first()  # Buscar usuario por ID
    if db_user:
        db.delete(db_user)  # Eliminar el usuario de la base de datos
        db.commit()  # Confirmar cambios
    return db_user
