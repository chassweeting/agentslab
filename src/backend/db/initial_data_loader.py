import json

from pathlib import Path

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from .database import get_db, init_db
from .models import MenuItem, Customer, Order, OrderItem



async def load_initial_data():
    print("Creating initial database")
    init_db()

    # Get a db session:
    db = get_db()
    load_regular_menus(db)
    load_customers(db)




def load_regular_menus(db: Session):

    path = Path(__file__).parent / "init_data" / "menu.json"
    with open(path) as f:
        json_data = json.load(f)

    availability_all_days = {
        'available_monday': True,
        'available_tuesday': True,
        'available_wednesday': True,
        'available_thursday': True,
        'available_friday': True,
        'available_saturday': True,
        'available_sunday': True
    }

    for category, items in json_data.items():
        for item in items:
            # Create a MenuItem instance with data from JSON and set it to be available every day
            menu_item = MenuItem(
                name=item['name'],
                price=item['price'],
                ingredients=', '.join(item['ingredients']),
                category=category,
                labels=item['label'],
                **availability_all_days
            )
            # Add the menu item to the session
            db.add(menu_item)

    # Commit the session to save all the new records to the database
    db.commit()


def load_customers(db: Session):

    path = Path(__file__).parent / "init_data" / "customers.json"
    with open(path) as f:
        json_data = json.load(f)

    try:
        # Iterate over each customer in the JSON data
        for customer in json_data:
            # Flatten the nested address into individual fields
            address = customer['address']
            customer_record = Customer(
                firstname=customer['firstname'],
                lastname=customer['lastname'],
                email=customer['email'],
                external_id=customer['id'],
                card_digits=customer['card_digits'],
                street=address['street'],
                city=address['city'],
                state=address['state'],
                zip=address['zip'],
                country=address['country'],
                special=customer['special'].lower() == "true",  # Convert "true"/"false" string to Boolean
                phone=customer['phone']
            )
            # Add the customer record to the session
            db.add(customer_record)

        # Commit the session to save all the new records to the database
        db.commit()

    except Exception as e:
        db.rollback()
        print(f"Error loading data: {e}")

    finally:
        # Close the session
        db.close()

    print("Customer data has been loaded successfully.")