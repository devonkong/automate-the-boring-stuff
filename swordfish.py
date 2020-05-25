while True:
    print('Who are you?')
    name = input()
    if name != 'Devon':
        continue
    print('Hello, Devon. What is the password? (It is a fish).')
    password = input()
    if password == 'swordfish':
        break
print('Welcome, Devon.')
