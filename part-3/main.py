from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name  : str
    desc  : Optional[str] = None
    price : float
    tax   : Optional[float] = None



app= FastAPI()



@app.post("/item/")
async def create_Item(item:Item):
    return item

