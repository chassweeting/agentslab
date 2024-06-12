from typing import Optional
from langchain.tools import tool
from langchain.pydantic_v1 import BaseModel, Field

class ScheduleToolInputSchema(BaseModel):
    day_of_week: str = Field(description="The day of the week for which you want the opening hours.")
    user_id: Optional[str] = Field(description="The optional user id in form '#<4-digits-number>'. (e.g. #1234)")


