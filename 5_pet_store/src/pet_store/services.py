from datetime import datetime
from typing import List, Type

from sqlalchemy.orm import Session

from pet_store.model import PetModel
from pet_store.schemas import PetCreate, Pet, PetUpdate


def get_pet(db: Session, pet_id: int) -> Pet:
    pass


def get_pet_by_name(db: Session, name: str) -> Pet:
    pass


def get_pets_by_date(db: Session, created_after: datetime) -> List[Pet]:
    pass


def get_all_pets(db: Session, skip: int = 0, limit: int = 100) -> list[Type[PetModel]]:
    return db.query(PetModel).offset(skip).limit(limit).all()


def add_pet(db: Session, pet: PetCreate) -> PetModel:
    pass


def update_pet(db: Session, pet: Pet, pet_update: PetUpdate) -> PetModel:
    pass


def remove_pet(db: Session, pet: PetModel) -> PetModel:
    pass
