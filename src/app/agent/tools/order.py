import requests
import json

from typing import List, Dict, Any, Optional
from langchain.pydantic_v1 import BaseModel, Field

#
# # Define the input schema for the order retrieval tool
# @tool("DailyMenuTool", args_schema=DailyMenuInputSchema)
# class OrderRetrievalToolInputSchema(BaseModel):
#     user_id: str = Field(description="The user id in form '#<4-digits-number>'. (e.g. #1234)")
#     credit_card_digits: str = Field(
#         description="The last 4 digits of the credit card number in form '####' (e.g. 1234)")
#     order_id: Optional[str] = Field(
#         description="The id of the open order to cancel in form '<4-digits-number>' (e.g. 8642)")
#
#
# class OrderCancellationToolInputSchema(BaseModel):
#     user_id: str = Field(description="The user id in form '#<4-digits-number>'. (e.g. #1234)")
#     credit_card_digits: str = Field(
#         description="The last 4 digits of the credit card number in form '####' (e.g. 1234)")
#     order_id: str = Field(description="The id of the open order to cancel in form '<4-digits-number>' (e.g. 8642)")

# @tool("order-retrieval-tool", args_schema=OrderRetrievalToolInputSchema)
# def order_retrieval(user_id:str, credit_card_digits:int, order_id:str=None):
#     """Useful when you need to retrieve the list of pending orders or a specific order of a user."""
#
#     # Check if the user id is authorized to retrieve the orders
#     response=check_autorization(user_id, credit_card_digits)
#     if response.status=="failed":
#         return response
#     if order_id is None:
#         return db.get_orders(user_id=user_id, status="pending")
#     else:
#         return db.get_order(user_id=user_id, order_id=order_id, status="pending")
#
# @tool("order-cancellation-tool", args_schema=OrderCancellationToolInputSchema)
# def order_cancellation(user_id:str, credit_card_digits:int, order_id:str):
#     """Useful when you need to cancel a specific pending order."""
#
#     # Check if the user id is authorized to cancel the order
#     response=check_autorization(user_id, credit_card_digits)
#     if response.status=="failed":
#         return response
#
#     # Delete the specified order by marking it as deleted in the database
#     return db.cancel_order(user_id=user_id, order_id=order_id)
#

def create_order(customer_id: int, items: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Create a new order for a customer.

    Args:
        customer_id (int): The ID of the customer.
        items (List[Dict[str, Any]]): A list of items with menu_item_id and quantity.

    Returns:
        Dict[str, Any]: The created order details.
    """
    url = f"http://localhost:8000/api/orders"
    payload = {
        'customer_id': customer_id,
        'items': items
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()


def check_order_status(order_id: int) -> Dict[str, Any]:
    """
    Check the status of an order by its ID.

    Args:
        order_id (int): The ID of the order.

    Returns:
        Dict[str, Any]: The order status and details.
    """
    url = f"http://localhost:8000/api/orders/{order_id}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()


