from datetime import datetime
from typing import List

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_204_NO_CONTENT

from pet_store.db import SessionLocal, engine
from pet_store import model
from pet_store.schemas import PetCreate, Pet, PetUpdate
from pet_store.services import get_pet_by_name, add_pet, get_pet, get_pets, get_pets_by_date, update_pet, remove_pet

model.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/pets/", response_model=Pet)
def create_pet(pet: PetCreate, db: Session = Depends(get_db)):
    db_pet = get_pet_by_name(db, name=pet.name)
    if db_pet:
        raise HTTPException(status_code=409, detail="Pet with that name already exists")
    return add_pet(db=db, pet=pet)


@app.delete("/pets/{pet_id}", status_code=HTTP_204_NO_CONTENT, response_model={})
def delete_pet(pet_id: int, db: Session = Depends(get_db)):
    db_pet = get_pet(db, pet_id=pet_id)
    if not db_pet:
        raise HTTPException(status_code=404, detail="Couldn't find the pet to remove")
    remove_pet(db=db, pet=db_pet)


@app.get("/pets/", response_model=List[Pet])
def read_pets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_pets(db, skip=skip, limit=limit)


@app.get("/pets/by_date/{created_after}", response_model=List[Pet])
def read_pets_created_after(created_after: datetime, skip: int = 0, limit: int = 100,
              db: Session = Depends(get_db)):
    return get_pets_by_date(db, created_after=created_after)


@app.get("/pets/{pet_id}", response_model=Pet)
def read_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = get_pet(db, pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Couldn't find a pet with that ID")
    return pet


@app.put("/pets/{pet_id}", response_model=Pet)
def update_pet_by_id(pet_id: int, pet_update: PetUpdate, db: Session = Depends(get_db)):
    pet = get_pet(db, pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Couldn't find a pet with that ID")
    return update_pet(db=db, pet=pet, pet_update=pet_update)


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("pet_store.main:app", host="0.0.0.0", port=8000, reload=True)