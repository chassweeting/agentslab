from pydantic import BaseModel
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
