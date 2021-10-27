from typing import Optional , List
from fastapi import FastAPI
from pydantic import BaseModel ,EmailStr
from pydantic.errors import DecimalMaxDigitsError


app = FastAPI()

class Item(BaseModel):
    name:str
    description:Optional[str] = None
    price : float =None
    tax: Optional[float] = None
    tags : List[str] = []


class UserIn(BaseModel):
    username : str
    password : str
    email    : EmailStr
    full_name: Optional[str] = None

class UserOut(BaseModel):
    username   : str
    email      : EmailStr
    full_name  : Optional[str] = None

@app.post("/items/" , response_model= Item)
async def create_item(item : Item):
    return item

@app.post("/user/", response_model=UserOut)
async def create_user(user:UserIn):
    return user