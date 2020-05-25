# A function that returns all the items in a list separated by commas and a space,
# with 'and' inserted before the last item.

# Defining the function
def return_list(list_name):
    return_value = 'This list contains '
    for item in list_name[:-1]:
        return_value += f'{item}, '
    if len(list_name) > 1:
        return_value += f'and {list_name[-1]}.'
        return return_value
    # This prevents 'and' from printing when the list has only one item
    elif len(list_name) == 0:
        return_value = 'This list does not contain any items.'
        return return_value
    else:
        return_value += f'{list_name[0]}.'
        return return_value

# Assigning the lists
spam = ['apples', 'bananas', 'tofu', 'cats']
hobbits = ['sam', 'frodo', 'merry', 'pippin', 'bilbo']
numbers = [1, 23, 3.14, -42, -1.198]
empty_list = []
list_with_lists = [['harry', 'ron', 'hermione'], ['potter', 'weasley', 'granger']]
one_item = ['TheBoldTilde']

# Testing the funcion with various lists
print(return_list(spam))
print(return_list(hobbits))
print(return_list(numbers))
print(return_list(empty_list))
print(return_list(list_with_lists))
print(return_list(one_item))

