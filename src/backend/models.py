from sqlalchemy import Column, Integer, String, Float, Boolean

from .database import Base

class MenuItem(Base):
    __tablename__ = 'menu_items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    ingredients = Column(String)
    category = Column(String)
    labels = Column(String)
    available_monday = Column(Boolean, default=False)
    available_tuesday = Column(Boolean, default=False)
    available_wednesday = Column(Boolean, default=False)
    available_thursday = Column(Boolean, default=False)
    available_friday = Column(Boolean, default=False)
    available_saturday = Column(Boolean, default=False)
    available_sunday = Column(Boolean, default=False)
