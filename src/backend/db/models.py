from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship

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

    order_items = relationship("OrderItem", back_populates="menu_item")  # One-to-many relationship


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    external_id = Column(String, unique=True, nullable=False)  # Corresponds to the "id" in JSON
    card_digits = Column(String, nullable=False)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip = Column(String, nullable=False)
    country = Column(String, nullable=False)
    special = Column(Boolean, default=False)
    phone = Column(String, nullable=True)

    orders = relationship("Order", back_populates="customer")  # One-to-many relationship



class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow)
    total_amount = Column(Float, nullable=False)

    customer = relationship("Customer", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")  # One-to-many relationship


class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    menu_item_id = Column(Integer, ForeignKey('menu_items.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    note = Column(Text, nullable=True)

    order = relationship("Order", back_populates="items")
    menu_item = relationship("MenuItem", back_populates="order_items")