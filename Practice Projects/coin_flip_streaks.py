# A program to find out how often a streak of six heads or tails occurs.

import random, re, numpy as np

print(f'Mathematically, the probability of a streak of six heads or tails occuring is {0.5**6 * 100: .2f}%')

streak_counter = []
streak_heads = r'HHHHHH'
streak_tails = r'TTTTTT'

for experiment in range(10):
    # Records occurences of heads or tails in a string.
    observations = ''
    for coin_flip in range(100):
        if random.randint(0, 1) == 0:
            observations += 'H'
        else:
            observations += 'T'
    
    # Checks for streaks of 6 heads or tails and adds to the counter.
    streak_counter.append(len(re.findall(streak_heads, observations)) + len(re.findall(streak_tails, observations)))
    print(f'The streak counter is now {streak_counter}.')
    
np.mean(streak_counter)

### Todo: Replace streak_counter with list and find mean.


print(f'The chance of 6 heads or tails occuring in a row is {sum(streak_counter)/100}%.')