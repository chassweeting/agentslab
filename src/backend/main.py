from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
# from azure.monitor.opentelemetry import configure_azure_monitor
from .routers import menu

from .initial_data_loader import load_initial_data
from .database import get_db
app = FastAPI()

@app.get("/hello")
def create_menu_item(db: Session = Depends(get_db)):
    return "hellow orld"


@app.on_event("startup")
async def startup_event():
    await load_initial_data()


origins = ["http://localhost:3000", "http://127.0.0.1:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(menu.router)

# @app.get("/menu-items/{day}", response_model=List[MenuItemCreate])
# def get_menu_items_for_day(day: str, db: Session = Depends(get_db)):
#     day_map = {
#         "Monday": MenuItem.available_monday,
#         "Tuesday": MenuItem.available_tuesday,
#         "Wednesday": MenuItem.available_wednesday,
#         "Thursday": MenuItem.available_thursday,
#         "Friday": MenuItem.available_friday,
#         "Saturday": MenuItem.available_saturday,
#         "Sunday": MenuItem.available_sunday
#     }
#
#     if day not in day_map:
#         raise HTTPException(status_code=400, detail="Invalid day")
#
#     items = db.query(MenuItem).filter(day_map[day] == True).all()
#     return items
