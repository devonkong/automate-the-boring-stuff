import random
number_of_streaks = 0

for experiment_number in range(10000):
    # This creates a list of 100 'heads' or 'tails' values
    coin_flip_results = []
    for coin_flip in range(100):
        if random.randint(0, 1) == 0:
            coin_flip_results.append('H')
        else:
            coin_flip_results.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row


print(f'The chance of 6 heads or tails occuring in a row is {number_of_streaks/100}.')
