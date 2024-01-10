from datetime import datetime
from typing import List, Type

from sqlalchemy.orm import Session

from pet_store.model import PetModel
from pet_store.schemas import PetCreate, Pet, PetUpdate


def get_pet(db: Session, pet_id: int) -> Pet:
    pet = db.query(PetModel).filter(PetModel.id == pet_id).first()
    return pet


def get_pet_by_name(db: Session, name: str) -> Pet:
    return db.query(PetModel).filter(PetModel.name == name).first()


def get_pets_by_date(db: Session, created_after: datetime) -> List[Pet]:
    return db.query(PetModel).filter(PetModel.created >= created_after).all()


def get_pets(db: Session, skip: int = 0, limit: int = 100) -> list[Pet]:
    return db.query(PetModel).offset(skip).limit(limit).all()


def add_pet(db: Session, pet: PetCreate) -> PetModel:
    db_pet = PetModel(name=pet.name, animal_type=pet.animal_type)
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet


def update_pet(db: Session, pet: Pet, pet_update: PetUpdate) -> Pet:
    if pet_update.name:
        pet.name = pet_update.name
    if pet_update.animal_type:
        pet.animal_type = pet_update.animal_type
    db.commit()
    return pet


def remove_pet(db: Session, pet: PetModel) -> None:
    db.delete(pet)
    db.commit()
