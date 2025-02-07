from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import config.db
import crud.users
import schemas.users
import models.user
from typing import List

user = APIRouter()

models.user.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

''' Se obtienen los datos de los usuarios '''
@user.get("/users/", response_model=List[schemas.users.User], tags=["usuarios"])
async def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_users = crud.users.get_users(db=db, skip=skip, limit=limit)
    return db_users
''' Post que trae los usuarios por id'''
@user.post("/user/{id}", response_model=schemas.users.User, tags=["usuarios"])
async def read_user(id:int, db:Session= Depends(get_db)):
    db_user = crud.users.get_user(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User already exists")
    return db_user

''' Registrar usuario normal'''
@user.post("/user/", response_model=schemas.users.User, tags=["usuarios"])
async def create_user(user: schemas.users.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.users.get_user_by_usuario(db, nombreUsuario=user.nombreUsuario)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return crud.users.create_user(db=db, user=user)

'''Actualizar usuario'''

@user.put("/user/{id}", response_model=schemas.users.User, tags=["usuarios"])
async def update_user(id: int, user:schemas.users.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.users.update_user(db=db, id=id, user=user)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User not exist, no Update")
    return db_user

@user.delete("/user/{id}", response_model=schemas.users.User, tags=["usuarios"])
async def delete_user(id: int, db: Session = Depends(get_db)):
    db_user = crud.users.delete_user(db=db, id=id)
    if db_user is None:
      raise HTTPException(status_code=400, detail="User not exist, no Update")
    return db_user

