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


# Checking for a phone number within a larger string

message = "Hi, I think you're cute. I'd like to meet you for coffee sometime. My phone number is 444-444-6969. Or you can call me at 414-414-4040 for... privacy reasons."

for i in range(len(message)):
    chunk = message[i:i + 12]
    if is_phone_number(chunk):
        print(f"Phone number found: {chunk}")
        
print("Done.")