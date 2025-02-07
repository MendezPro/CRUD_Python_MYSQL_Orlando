from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import config.db
import crud.materials
import schemas.material
import models.material
from typing import List

material = APIRouter()

models.material.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

''' Se obtienen los datos de los materiales '''
@material.get("/materials/", response_model=List[schemas.material.Material], tags=["materiales"])
async def read_materials(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_materials = crud.materials.get_materials(db=db, skip=skip, limit=limit)
    return db_materials

''' Post que trae los materiales por id'''
@material.post("/material/{id}", response_model=schemas.material.Material, tags=["materiales"])
async def read_material(id: int, db: Session = Depends(get_db)):
    db_material = crud.materials.get_material(db=db, id=id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material

''' Registrar material '''
@material.post("/material/", response_model=schemas.material.Material, tags=["materiales"])
async def create_material(material: schemas.material.MaterialCreate, db: Session = Depends(get_db)):
    return crud.materials.create_material(db=db, material=material)

''' Actualizar material '''
@material.put("/material/{id}", response_model=schemas.material.Material, tags=["materiales"])
async def update_material(id: int, material: schemas.material.MaterialUpdate, db: Session = Depends(get_db)):
    db_material = crud.materials.get_material(db=db, id=id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return crud.materials.update_material(db=db, material=material, id=id)

''' Eliminar material '''
@material.delete("/material/{id}", response_model=schemas.material.Material, tags=["materiales"])
async def delete_material(id: int, db: Session = Depends(get_db)):
    db_material = crud.materials.get_material(db=db, id=id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return crud.materials.delete_material(db=db, id=id)