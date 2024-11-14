def add_item(current_cart, items_to_add):
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1

    return current_cart

def read_notes(notes):
    user_cart = {}
    for item in notes:
        user_cart[item] = 1

    return user_cart

def update_recipes(ideas, recipe_updates):
    for key, value in recipe_updates:
        ideas[key] = value

    return ideas

def sort_entries(cart):
    return dict(sorted(cart.items()))

def send_to_store(cart, aisle_mapping):
    info_dict = {}
    for key, value in cart.items():
        info_dict[key] = [value] + aisle_mapping[key]

    return dict(sorted(info_dict.items(), reverse=True))

def update_store_inventory(fulfillment_cart, store_inventory):
    for key in fulfillment_cart:
        if store_inventory[key][0] != 'Out of Stock':
            new_stock = store_inventory[key][0] - fulfillment_cart[key][0]
            if new_stock <= 0:
                new_stock = 'Out of Stock'
            store_inventory[key][0] = new_stock

    return store_inventory