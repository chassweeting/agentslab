# Using Tools

Tools are just Python functions which we send to Azure OpenAI SDK

egion
Operative
Schedule
function


import json
import requests
from typing import List, Dict, Any

def get_menu_items(day: str, category: str) -> List[Dict[str, Any]]:
    """
    Get all menu items available on a specific day and in a specific category.

    Args:
        day (str): The day of the week (e.g., "Monday").
        category (str): The category of the menu items (e.g., "Pizza").

    Returns:
        List[Dict[str, Any]]: A list of menu items.
    """
    url = f"http://localhost:8000/api/menu_items"
    params = {'day': day, 'category': category}
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()

# Example usage:
menu_items = get_menu_items("Monday", "Pizza")
print(json.dumps(menu_items, indent=4))







# Function to get the current date and time in the format <day-name>, dd/mm/yyyy hh:mm
def get_current_datetime():
    local_tz = pytz.timezone(local_timezone)
    return json.dumps({
        "current_datetime": datetime.now(local_tz).strftime("%A, %d/%m/%Y %H:%M")
    })


# We create a dictionary with the available functions, using function name as key, note the new added functions "get_current_datetime"
available_functions = {
    "operative_schedule": operative_schedule,
    "get_menu": get_menu,
    "get_current_datetime": get_current_datetime
}