from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name    :str
    desc    :Optional[str]=None
    price   :float
    tax     :Optional[float]=None


class User(BaseModel):
    u_name      :str
    full_name   :Optional[str] = None

app=FastAPI()

@app.post("/item/{item_id}")
async def post_item(item_id : int , item : Item , user:User):
    #print(item)
    #print(user)
    results = {"item_id": item_id, "item": item, "user": user}
    return{"result":results}
