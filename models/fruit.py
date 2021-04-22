from typing import Optional
from pydantic import BaseModel

class Fruit(BaseModel):
    name: str
    quantity: int
    calories: int

class FruitUpdate(BaseModel):
    quantity: Optional[int] = None
