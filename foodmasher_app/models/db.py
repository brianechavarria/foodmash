from models.food import FoodItems

# dictionary: filename -> FoodItems instance
food_db = {}

def init_images(image_dir):
    import os
    images = [img for img in os.listdir(image_dir)]
    for name in images:
        if name not in food_db:
            food_db[name] = FoodItems(name)
