# Chapter 7: Finding patterns of text without regular expressions

def is_phone_number(input):
    if len(input) != 12:
        return False
    for i in range(0, 3):
        if not input[i].isdecimal():
            return False
    if input[3] != '-':
        return False
    for i in range(4, 7):
        if not input[i].isdecimal():
            return False
    if input[7] != '-':
        return False
    for i in range(8, 12):
        if not input[i].isdecimal():
            return False
    return True

test_input_1 = '415-555-2321'
test_input_2 = 'Welcome to the United States'

print(f"Is {test_input_1} a phone number?")
print(is_phone_number(test_input_1))

print(f"Is {test_input_2} a phone number?")
print(is_phone_number(test_input_2))