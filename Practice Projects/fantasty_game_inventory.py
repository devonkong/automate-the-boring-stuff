# Chapter 5: Fantasy Game Inventory
# The data structure is a dictionary where the keys are string values describing the item in the inventory,
# and the value is an integer value detailing how many of that item the player has.
# Write a function that takes an inventory and displays the quantity of each item and the name of the item in the inventory, and the total number of items.

# Creating the inventory dictionary based on items in my backpack
backpack = {'laptop': 1, 'usb stick': 2, 'pen': 2, 'face mask': 8, 'charging cable': 2, 'bottle': 1, 'hand sanitiser': 2}

def display_inventory(inventory):
    """Takes a dictionary as an argument and returns the value followed by the key as a string value for each item in the dictionary."""
    
    print('Inventory:')
    
    total_items = 0
    
    for item, quantity in inventory.items():
        total_items += quantity
        if quantity == 1:
            print(f"{quantity} {item}")
        else:
            print(f"{quantity} {item}s")
            
    print(f"Total items: {total_items}")

print("This is what's in my backpack today.", end = '\n\n')
display_inventory(backpack)
    

# Chapter 5: List to Dictionary Function for Fantasy Game Inventory
# Write a function that accepts two parameters (dictionary, list) that addes the items in the list to the dictionary and returns an updated dictionary.

# Creating a list of items I picked up at the supermarket (yes, my fantasty game is not very fantastical)
grocery_run = ['milk', 'egg', 'egg', 'chicken', 'egg', 'milk', 'egg', 'chocolate', 'egg', 'spinach', 'butter', 'egg', 'egg', 'pen']

def add_to_inventory(inventory, new_items):
    for item in new_items:
        # If item doesn't exist in inventory, create a new key with a value of 0
        inventory.setdefault(item, 0)
        inventory[item] += 1
             
    return inventory

add_to_inventory(backpack, grocery_run)
print("\nI did a grocery run, and stuffed the new items into my backpack.", end = '\n\n')
display_inventory(backpack)
    