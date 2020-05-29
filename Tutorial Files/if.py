# This program checks your name and age with if, elif and else statements.

print('What is your name?')
name = input()

print('How old are you?')
age = int(input())


if name == 'Devon':
    print('Hi Devon!')
elif age < 12:
    print('You are not Wolf, kiddo.')
elif age > 100:
    print('Wolf is old, but not THAT old.')
elif name == 'Wolf':
    print('Hi Wolf!')
else:
    print('You are neither Devon nor Wolf.')
