from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import config.db
import crud.prestamos
import schemas.prestamo
import models.prestamo
from typing import List

prestamo = APIRouter()

models.prestamo.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

''' Se obtienen los datos de los prestamos '''
@prestamo.get("/prestamos/", response_model=List[schemas.prestamo.Prestamo], tags=["prestamos"])
async def read_prestamos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_prestamos = crud.prestamos.get_prestamos(db=db, skip=skip, limit=limit)
    return db_prestamos

''' Post que trae los prestamos por id'''
@prestamo.post("/prestamo/{id}", response_model=schemas.prestamo.Prestamo, tags=["prestamos"])
async def read_prestamo(id: int, db: Session = Depends(get_db)):
    db_prestamo = crud.prestamos.get_prestamo(db=db, id=id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo not found")
    return db_prestamo

''' Registrar prestamo '''
@prestamo.post("/prestamo/", response_model=schemas.prestamo.Prestamo, tags=["prestamos"])
async def create_prestamo(prestamo: schemas.prestamo.PrestamoCreate, db: Session = Depends(get_db)):
    return crud.prestamos.create_prestamo(db=db, prestamo=prestamo)

''' Actualizar prestamo '''
@prestamo.put("/prestamo/{id}", response_model=schemas.prestamo.Prestamo, tags=["prestamos"])
async def update_prestamo(id: int, prestamo: schemas.prestamo.PrestamoUpdate, db: Session = Depends(get_db)):
    db_prestamo = crud.prestamos.get_prestamo(db=db, id=id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo not found")
    return crud.prestamos.update_prestamo(db=db, prestamo=prestamo, id=id)

''' Eliminar prestamo '''
@prestamo.delete("/prestamo/{id}", response_model=schemas.prestamo.Prestamo, tags=["prestamos"])
async def delete_prestamo(id: int, db: Session = Depends(get_db)):
    db_prestamo = crud.prestamos.get_prestamo(db=db, id=id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo not found")
    return crud.prestamos.delete_prestamo(db=db, id=id)