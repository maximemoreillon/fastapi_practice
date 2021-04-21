from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from controllers import fruits as controller

router = APIRouter()

class Fruit(BaseModel):
    name: str

@router.get("/")
async def get_all_fruits():
    results = controller.read_all_fruits()
    return results

@router.post("/")
async def create_fruit(new_fruit: Fruit):
    results = controller.create_fruit(new_fruit)
    return results
