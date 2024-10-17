from cater_waiter_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)

def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name, set(dish_ingredients))

def check_drinks(drink_name, drink_ingredients):
    if ALCOHOLS.isdisjoint(drink_ingredients):
        drink_suffix = "Mocktail"
    else:
        drink_suffix = "Cocktail"

    return drink_name + " " + drink_suffix

def categorize_dish(dish_name, dish_ingredients):
    dish_categories = (VEGAN, VEGETARIAN, PALEO, KETO, OMNIVORE)
    category_strings = ("VEGAN", "VEGETARIAN", "PALEO", "KETO", "OMNIVORE")
    for index, category in enumerate(dish_categories):
        if category.issuperset(dish_ingredients):
            result_string = f"{dish_name}: {category_strings[index]}"

    return result_string

def tag_special_ingredients(dish):
    return (dish[0], set(dish[1]).intersection(SPECIAL_INGREDIENTS))

def compile_ingredients(dishes):
    compiled_list = set()
    for dish in dishes:
        compiled_list = compiled_list.union(dish)

    return compiled_list

def separate_appetizers(dishes, appetizers):
    return list(set(dishes).difference(appetizers))

def singleton_ingredients(dishes, intersection):
    ingredients_list = []
    for dish in dishes:
        for ingredient in dish:
            ingredients_list.append(ingredient)

    return intersection.symmetric_difference(ingredients_list)