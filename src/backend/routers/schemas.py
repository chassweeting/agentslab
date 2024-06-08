from pydantic import BaseModel, EmailStr
from typing import Optional


class MenuItem(BaseModel):
    name: str
    price: float
    ingredients: str
    category: str
    labels: Optional[str] = None
    available_monday: bool = False
    available_tuesday: bool = False
    available_wednesday: bool = False
    available_thursday: bool = False
    available_friday: bool = False
    available_saturday: bool = False
    available_sunday: bool = False

    class Config:
        orm_mode = True


class CustomerBase(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    phone: Optional[str] = None
    special: Optional[bool] = False
    card_digits: str
    external_id: str
    street: str
    city: str
    state: str
    zip: str
    country: str

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    firstname: Optional[str]
    lastname: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[str]
    special: Optional[bool]
    card_digits: Optional[str]
    street: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip: Optional[str]
    country: Optional[str]

class CustomerInDB(CustomerBase):
    id: int

    class Config:
        orm_mode = True

