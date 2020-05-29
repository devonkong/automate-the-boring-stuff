def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number >= 0 and number % 2 == 1:
        return 3 * number + 1
    elif number < 0 and number % 2 == 1:
        return 3 * number - 1


print('Hello, please enter a number.')

import sys

while True:
    while True:
        try:
            initial_number = int(input())
            break

        except ValueError:
            print('You did not enter a number. Please try again.')

    while True:
        initial_number = collatz(initial_number)
        print(initial_number)
        if abs(initial_number) == 1:
            break

    print('The Collatz sequence has returned a value of 1.')

    while True:
        print('Type Y to try again with a different number, or N to exit.')
        repeat_or_exit = input()
        if repeat_or_exit == 'Y':
            print('Please enter a number.')
            break
        elif repeat_or_exit == 'N':
            print('Thank you for participating.')
            sys.exit()
        else:
            print('You did not type either Y or N.')


