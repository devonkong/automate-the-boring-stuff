import random, sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0


while True: # This is the main game loop.
    print()
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    print()
    while True: #This is the player input loop.
        print('Enter R for rock, P for paper, or S for scissors.')
        print('To quit, enter Q.')
        print()

        player_move = input()
        print()
        if player_move == 'Q':
            sys.exit() # This terminates the program.
        if player_move == 'R' or player_move == 'P' or player_move == 'S':
            break # This breaks the player input loop.

    # This displays what the player chose.
    if player_move == 'R':
        print('You throw out rock!')
    elif player_move == 'P':
        print('You throw out paper!')
    elif player_move == 'S':
        print('You throw out paper!')

    # This displays what the computer chose.
    random_number = random.randint(1,3)
    if random_number == 1:
        computer_move = 'R'
        print('Computer used rock!')
    if random_number == 2:
        computer_move = 'P'
        print('Computer used paper!')
    if random_number == 3:
        computer_move = 'S'
        print('Computer used scissors!')

    print()

    # This displays and records the score.
    if player_move == computer_move:
        print('You tied!')
        ties += 1
    elif player_move == 'R' and computer_move == 'S':
        print('You win!')
        wins += 1
    elif player_move == 'P' and computer_move == 'R':
        print('You win!')
        wins += 1
    elif player_move == 'S' and computer_move == 'P':
        print('You win!')
        wins += 1
    elif player_move == 'R' and computer_move == 'P':
        print('You lose!')
        losses += 1
    elif player_move == 'P' and computer_move == 'S':
        print('You lose!')
        losses += 1
    elif player_move == 'S' and computer_move == 'R':
        print('You lose!')
        losses += 1



