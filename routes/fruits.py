from fastapi import APIRouter, HTTPException
from controllers import fruits as controller
from models.fruit import Fruit, FruitUpdate

router = APIRouter()


@router.get("/")
async def get_all_fruits():
    results = controller.read_all_fruits()
    return results

@router.post("/")
async def create_fruit(new_fruit: Fruit):
    results = controller.create_fruit(new_fruit)
    return results

@router.get("/{index}")
async def get_fruit(index: int):
    results = controller.read_fruit(index)
    return results

@router.put("/{index}")
async def put_fruit(index: int, new_fruit: Fruit):
    results = controller.replace_fruit(index, new_fruit)
    return results

@router.patch("/{index}")
async def patch_fruit(index: int, properties: FruitUpdate):
    results = controller.update_fruit(index, properties)
    return results
