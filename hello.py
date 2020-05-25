# This program says hello and asks for your name.

print('Hello and welcome!')


print('What is your name, friend?') # Asking for name
print()

name = input()
print()

print('Hi, ' + name +'!')
print('Your name has ' + str(len(name)) + ' letters. That means you will have good luck today.')
print()


print('How old are you?')  # Asking for age
print()

age = input()
print()

print('You are ' + str(int(age) + 100) + '? That is pretty fucking old!')
