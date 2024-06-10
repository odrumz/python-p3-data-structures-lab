spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [getname["name"] for getname in spicy_foods]
    

def get_spiciest_foods(spicy_foods):
    return [spiciest for spiciest in spicy_foods if spiciest['heat_level']>5 ]
 

def print_spicy_foods(spicy_foods):
     for spicy in spicy_foods:
        print(f"{spicy['name']} ({spicy['cuisine']}) | Heat Level: {'🌶'* spicy['heat_level']}" )

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
     for type in spicy_foods:
         if type["cuisine"] == cuisine:
             return type
     return None

         
def print_spiciest_foods(spicy_foods):
     for food in spicy_foods:
         if food["heat_level"] > 5:
             print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")


# def get_average_heat_level(spicy_foods):
#     pass

# def create_spicy_food(spicy_foods, spicy_food):
#     pass

def get_average_heat_level(spicy_foods):
    
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)



def create_spicy_food(spicy_foods, spicy_food):

    spicy_foods.append(spicy_food)
    return spicy_foods
