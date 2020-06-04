# Chapter 6: Table Printer
# Write a function that takes a list of lists of strings and displayes it in a well organized table with each column right-justified.

table_data = [['Harry', 'Hermione', 'Ron', 'Luna'],
              ['steamed fish', 'chocolate', 'hotdog', 'croissant'],
              ['animation', 'psychology', 'programming', 'statistics']]

def print_table(table):
    """Prints the string values in the arg list of lists as a neat table."""
    
    # Loop over the string values in the list of lists and record the length of each word.
    col_widths = []
    for index in range(len(table)):
        letter_count = []
        for item in range(len(table[index])):
            letter_count.append(len(table[index][item]))
        col_widths.append(letter_count)
        
    # Get the length of the longest word in each column.
    for index in range(len(col_widths)):
        col_widths[index] = max(col_widths[index])
        
    # Create an empty list to store the lists of formatted data.
    padding = 3
    formatted_table = []
    
    for index in range(len(table)):
        formatted_table.append([])  # Create and append an empty list to store the formatted data
        for item in range(len(table[index])):
            # Right-justify the string values based on the longest string value stored within col_widths
            formatted_table[index].append(table[index][item].rjust(col_widths[index] + padding))
            
    # Print a title for the table.
    # Padding calculated based on number of columns and the extra '|' added for formatting.
    print('VERY NEAT TABLE'.center(sum(col_widths) + ((padding + 1) * len(formatted_table)) + 1, '-'))  
            
    # Print the formatted text. 
    for index in range(len(formatted_table)):
        print('|', end = '')
        for list in formatted_table:
            print(list[index], end = '|')
        print()
    
print_table(table_data)