from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from pet_store.db import SessionLocal, engine
from pet_store import model
from pet_store.schemas import PetCreate, Pet
from pet_store.services import get_all_pets

model.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/pets", response_model=List[Pet])
def get_pets(limit: int = 100, db: Session = Depends(get_db)):
    return get_all_pets(db, limit=limit)


@app.get("/pets/{pet_id}")
def get_pet(pet_id):
    return {'message': f'TBD'}, 501


@app.delete("/pets/{pet_id}")
def delete_pet(pet_id):
    return {'message': f'TBD'}, 501


@app.post("/pets/", response_model=Pet)
def create_pet(pet: PetCreate, db: Session = Depends(get_db)):
    return {'message': f'TBD'}, 501



@app.get("/pets/by_date/{creation_date}")
def get_pet_after_creation_date(creation_date):
    return {'message': f'TBD'}, 501
