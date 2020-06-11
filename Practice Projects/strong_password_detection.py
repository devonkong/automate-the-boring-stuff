# Chapter 7: Strong Password Detection
# Write a function that uses regex to check that a passowrd is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit.

import re


# Passwords to be tested
sample_passwords = ['password', 'p4ssw0rd', 'P4ssw0rd', 'PaSsWoRd', '12345', '12345678', 'password1234', 'Password1234', 'PaSSw0rD321', 'password!', 'P@ssw0rd!', '@!@#$#%#^#@']


# Function that carries out test
def is_password_strong(password):
    """Checks that passowrd is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit."""
    
    # Validate that password is more than 8 characters long and is not entirely uppercase or lowercase
    if len(password) >= 8 and not password.isupper() and not password.islower():
        # Validate that password contains both letters and digits
        if re.compile(r'[a-zA-Z]').search(password) != None and re.compile(r'\d').search(password) != None:
            return True    
    # Return False if password does not pass any of the conditions    
    return False


# Test strong password regex
for password in sample_passwords:
    print(password, is_password_strong(password))
    
