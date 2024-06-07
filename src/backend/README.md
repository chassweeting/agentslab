# Persistence layer 


## Example usage 

```python 

from backend.database import get_db, init_db
from backend.models import MenuItem 

# Create the database tables if they doesn't exist 
init_db()

# Create an instance of the 
item = MenuItem(name="fanta", price=2.99) 

# Create a database session and persist the item 
db = get_db() 
db.add(item) 
db.commit() 

# Query for the menu items 
results = db.query(MenuItem).all() 

```