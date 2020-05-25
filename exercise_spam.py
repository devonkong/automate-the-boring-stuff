# Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

import random

spam = random.randint(1,3)

if spam == 1:
    print('Hello!')

elif spam == 2:
    print('Howdy!')

else:
    print('Greetings!')

print(str(spam))
