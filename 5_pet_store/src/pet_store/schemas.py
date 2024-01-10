from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class PetBase(BaseModel):
    name: str = Field(None, title="The name of the pet", max_length=100)
    animal_type: str = Field(None, title="The type of the pet (one of dog, cat, fish)")


class PetCreate(PetBase):
    pass


class PetUpdate(BaseModel):
    name: str = Field(None, title="The name of the pet", max_length=100)
    animal_type: Optional[str] = None


class Pet(PetBase):
    id: int
    created: Optional[datetime] = None

    class Config:
        orm_mode = True
