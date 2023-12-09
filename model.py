from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class Formulario(BaseModel):
    name: str = Field(min_length=1)
    age: str = Field(min_length=1)
    email: EmailStr = Field(min_length=1)
    person_number: int = Field(ge=1, le=100)
    adult_number: int = Field(ge=1, le=100)
    children_number: int = Field(ge=1, le=100)
    destiny: str = Field(min_length=1)
    duration: int = Field(ge=1, le=100)
    start_date: str = Field(min_length=1)
    end_date:str = Field(min_length=1)
    experiences:str = Field(min_length=1)