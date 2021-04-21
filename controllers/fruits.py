

fruits = [{'name': 'banana'},{'name': 'orange'}]



def read_all_fruits():
    return fruits

def create_fruit(new_fruit):
    fruits.append(new_fruit)
    return fruits
