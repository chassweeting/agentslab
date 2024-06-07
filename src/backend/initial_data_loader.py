import json

from .database import get_db, init_db
from .models import MenuItem
from sqlalchemy.exc import IntegrityError

async def load_initial_data():
    print("Creating initial database")
    init_db()

    print("Loading initial data")
    db = get_db()
    try:
        item = MenuItem(name="tiaramu", price=2.09)
        db.add(item)
        try:
            db.commit()
        except IntegrityError:
            db.rollback()
    finally:
        db.close()
