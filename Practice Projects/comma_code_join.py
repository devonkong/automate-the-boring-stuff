# A function that returns all the items in a list separated by commas and a space,
# with 'and' inserted before the last item.


# Defining a function that looks checks for lists within a list and flattens it (Thanks u/PyTec-Ari)
def flatten_list(list_input):
    output = []
    for item in list_input:
        if type(item) == list:
            output += flatten_list(item)
        else:
            output.append(item)
    return output


# Defining a function that neatly formats the items in a list
def format_list(list_input):
    # This joins all items in the list, separated by ', ', except the last item
    # Added str() to deal with TypeError when lists contain integers
    formatted_list = ', '.join(str(item) for item in list_input[:-1])
    # This adds 'and ' before the last item
    if len(list_input) > 1:
        formatted_list += f' and {list_input[-1]}'
        return formatted_list
    # This returns 'nothing' if the list is empty
    elif len(list_input) == 0:
        return 'nothing'
    else:
        formatted_list += f'{list_input[0]}'
        return formatted_list
    

# Defining a function that calls flatten_list() and format_list() then prints the results
def print_list(list_input):
    formatted_list = format_list(flatten_list(list_input))
    print(f"This list contains {formatted_list if formatted_list else 'nothing'}.")
   

# Assigning the lists
hobbits = ['sam', 'frodo', 'merry', 'pippin', 'bilbo']
numbers = [1, 23, 3.14, -42, -1.198]
empty_list = []
wizards = [['harry', 'ron', 'hermione'], ['potter', 'weasley', 'granger']]
one_item = ['TheBoldTilde']


# Testing the funcion with various lists
print_list(hobbits)
print_list(numbers)
print_list(empty_list)
print_list(wizards)
print_list(one_item)

