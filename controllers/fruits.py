from models.fruit import Fruit

fruits = [
    {'name': 'banana', 'quantity': 1},
    {'name': 'orange', 'quantity': 2},
]

def read_all_fruits():
    return fruits

def create_fruit(new_fruit):
    fruits.append(new_fruit)
    return fruits

def read_fruit(index):
    return fruits[index]

def replace_fruit(index, new_fruit):
    fruits[index] = new_fruit
    return fruits[index]

def update_fruit(index, properties):
    # This is equivalentto getting an Item from the DB and turning it into the same format as the model
    stored_item_data  = fruits[index] # Get the item from the array
    stored_item_model = Fruit(**stored_item_data) # **stored_item_data => name=fruitName, quantity=fruitQuantity

    # Handling of the data passed by the API
    update_data = properties.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)

    fruits[index] = updated_item
    return fruits[index]

def delete_Fruit(index):
    return fruits[index]
