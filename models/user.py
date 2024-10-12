from pydantic import BaseModel,Field
from typing import Optional
from datetime import datetime
class User(BaseModel):
    email   :   str
    location    : str
    clock_in : str = Field(default_factory=datetime.now)

class Item(BaseModel):
    email   :   str
    name    : str
    item_name : str
    expiry_date : str
    quantity : int
    insert_date : str = Field(default_factory=datetime.now)
