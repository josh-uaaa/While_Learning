def create_inventory(items):
    inventory_dict = {}
    for item in items:
        if item in inventory_dict:
            inventory_dict[item] += 1
        else:
            inventory_dict[item] = 1

    return inventory_dict

def add_items(inventory, items):
    for item in items:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory

def decrement_items(inventory, items):
    for item in items:
        if item in inventory.keys() and inventory[item] > 0:
            inventory[item] -= 1

    return inventory

def remove_item(inventory, item):
    inventory.pop(item, "not in list")
    return inventory

def list_inventory(inventory):
    inventory_list = []
    for key in inventory:
        if inventory[key] > 0:
            inventory_list.append((key, inventory[key]))

    return inventory_list