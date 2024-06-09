from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from .routers import menu_items, customers, orders

from .db.initial_data_loader import load_initial_data


app = FastAPI()


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


app.include_router(customers.router, prefix="/api", tags=["Customers"])
app.include_router(menu_items.router, prefix="/api")
app.include_router(orders.router, prefix="/api", tags=["Orders"])
