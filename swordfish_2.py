name = ''
password = ''

while name != 'Devon':
    print('What is your name?')
    name = input()

print('Welcome back, Devon! Please enter your password.')

while True:
    password = input()
    if password == 'swordfish':
        break
    print('That is incorrect. Please try again.')

print('That is correct. Good job!')
