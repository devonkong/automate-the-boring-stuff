# Chapter 7: Regex version of the strip() method
# Write a function that takes a string and does the same thing as the strip() method

import re


# Define function that strips characters from the start and end of a string
def regex_strip(string, char = '\s'):
    """
    Strips char from start and end of string.
    
    Args:
        string: A string value to be formatted.
        char: The characters to be removed. Characters are removed from string regardless of order. Defaults to whitespace.
    
    Returns:
        A string value with char removed from the start and end.
    """
    
    # Formats the characters into a regex class with caret and dollar symbols signifying the start and end
    regex_start = '^[' + char + ']*'
    regex_end = '[' + char + ']*$'

    # Removes char from start and end of string
    formatted_string = re.compile(regex_start).sub('', string)
    formatted_string = re.compile(regex_end).sub('', formatted_string)

    return formatted_string
    

# Test function
print(regex_strip("   white space   "))
print(regex_strip("www.devonkong.com", "www.com"))
print(regex_strip("***starman***", "*"))
print(regex_strip("  How are you, buddy? !?   @", "@ ?!"))
