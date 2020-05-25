# A program to find out how often a streak of six heads or tails occurs.

import random, re

streak_counter = 0
streak_heads = r'HHHHHH'
streak_tails = r'TTTTTT'

for experiment in range(1):
    # Records occurences of heads or tails in a string.
    observations = ''
    for coin_flip in range(100):
        if random.randint(0, 1) == 0:
            observations += 'H'
        else:
            observations += 'T'
    
    # Checks for streaks of 6 heads or tails and adds to the counter.
    print(observations)
    streak_counter += len(re.findall(streak_heads, observations))\
                       + len(re.findall(streak_tails, observations))
    print(f'The streak counter is now {streak_counter}.')
    

### Todo:   Replace streak_counter with list and find mean.
###         Estimate percentage mathematically to test accuracy of results.


print(f'The chance of 6 heads or tails occuring in a row is {streak_counter/100}%.')
