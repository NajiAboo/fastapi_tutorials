from fastapi import FastAPI
from pydantic import BaseModel

class Items(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    final_price: float | None = None


app = FastAPI()

@app.post("/items/")
async def save_item(item: Items):
    item.final_price = item.price * item.tax
    return item