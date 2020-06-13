# Chapter 8: Sandwich Maker
# Write a program that asks users for their sandwich preferences, and displays a total cost after the user enters their selection

import pyinputplus as pyip

# Set menu and prices
menu = {'bread': {'multigrain': 2.00, 'white': 1.00, 'wrap': 1.00},
          'protein': {'chicken': 1.00, 'meatballs': 2.00, 'tuna': 1.00, 'turkey': 1.50},
          'cheese': {'cheddar': 1.00, 'swiss': 2.00, 'tasty': 1.00},
          'salad': {'lettuce': 0.50, 'tomato': 0.50, 'avocado': 2.00},
          'sauce': {'mayo': 0.00, 'mustard': 0.00, 'ketchup': 0.00}}

# Create empty dictionary for customer order
order = {}

employee = {'name': 'Devon', 'position': 'Sandwich Artiste'}
print(f"Welcome to Subway. My name is {employee['name']} and I'm a {employee['position']}.")


# Create function that asks for customer choice and records in order dictionary
def customer_choice(option):
    """Asks user which type of option they would like from the menu dict, then records selection in order dict."""
    
    print(f'\nWhat type of {option} would you like?')
    chosen_option = (pyip.inputMenu(choices = list(menu[option].keys()), numbered = True))
    order.setdefault(chosen_option, menu[option][chosen_option])

    
# Ask for bread and protein type
customer_choice('bread')
customer_choice('protein')

# Ask if user wants cheese, and if so what type
if pyip.inputYesNo('\nAnd would you like cheese with your sandwich today?') == 'yes':
    customer_choice('cheese')
else:
    print('Alright, no cheese on this sandwich.')

# Ask if user wants mayo, mustard, lettuce, or tomato
customer_choice('salad')
customer_choice('sauce')

# Ask how many sandwiches user wants
number_of_sandwiches = pyip.inputInt('\nGreat! And how many of these sandwiches would you like?', min = 1)

# Calculate cost of sandwich
cost_of_sandwich = sum(order.values())


# Display order total
print(f"""
Your order comes to a total of ${cost_of_sandwich * number_of_sandwiches:.2f} for {number_of_sandwiches} sandwiches.
Please come again!""")