from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel ,HttpUrl

app=FastAPI()


class Image(BaseModel):
    url : HttpUrl
    name : str




class Item(BaseModel):
    name : str
    description : Optional[str] = None
    price : float = None
    tax :Optional[float] = None
    tags : List = []
    image : Optional[Image] = None

@app.put("/items/{item_id}")
async def item_update(item_id : int , item : Item):
    result = {"ID":item_id , "Item":item}
    return result
    

# need req body  
@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images