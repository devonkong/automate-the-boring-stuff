the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def print_board(board):
    print(f" {board['top-L']} | {board['top-M']} | {board['top-R']} ")
    print('–––+–––+–––')
    print(f" {board['mid-L']} | {board['mid-M']} | {board['mid-R']} ")
    print('–––+–––+–––')
    print(f" {board['low-L']} | {board['low-M']} | {board['low-R']} ")
    
turn = 'X'
for i in range(9):
    print_board(the_board)
    print(f"\nIt is {turn}'s turn. Which space would you like to select?\n")
    move = input()
    the_board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    
print_board(the_board)