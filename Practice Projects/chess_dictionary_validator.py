# Chapter 5: Chess Dictionary Validator
# Write a function that takes a dictionary argument and returns a Boolean value depending on if the board is valid.
# This function should detect when a bug has resulted in an improper chess board.
 
    
# Creating a list of valid coordinates on a chess board
valid_coordinates = []
for number in [8, 7, 6, 5, 4, 3, 2, 1]:
    for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        valid_coordinates.append(str(number) + letter)
    
# A dictionary representing a chess board with pieces in their starting positions
chess_board = {'8a': 'b-rook', '8b': 'b-knight', '8c': 'b-bishop', '8d': 'b-queen', '8e': 'b-king', '8f': 'b-bishop', '8g': 'b-knight', '8h': 'b-rook',
               '7a': 'b-pawn', '7b': 'b-pawn', '7c': 'b-pawn', '7d': 'b-pawn', '7e': 'b-pawn', '7f': 'b-pawn', '7g': 'b-pawn', '7h': 'b-pawn',
               '6a': '', '6b': '', '6c': '', '6d': '', '6e': '', '6f': '', '6g': '', '6h': '',
               '5a': '', '5b': '', '5c': '', '5d': '', '5e': '', '5f': '', '5g': '', '5h': '',
               '4a': '', '4b': '', '4c': '', '4d': '', '4e': '', '4f': '', '4g': '', '4h': '',
               '3a': '', '3b': '', '3c': '', '3d': '', '3e': '', '3f': '', '3g': '', '3h': '',
               '2a': 'w-pawn', '2b': 'w-pawn', '2c': 'w-pawn', '2d': 'w-pawn', '2e': 'w-pawn', '2f': 'w-pawn', '2g': 'w-pawn', '2h': 'w-pawn',
               '1a': 'w-rook', '1b': 'w-knight', '1c': 'w-bishop', '1d': 'w-queen', '1e': 'w-king', '1f': 'w-bishop', '1g': 'w-knight', '1h': 'w-rook'}


def is_valid_chess_board(board):
    """A function that returns True or False depending on the validity of the argument board."""
    
    # Create a dictionary to record the pieces on the chess board
    # Note: Each player must have exactly one king, at most 16 pieces and at most 8 pawns
    piece_counter = {'b-king': 0, 'b-pieces': 0, 'b-pawns': 0,
                            'w-king': 0, 'w-pieces': 0, 'w-pawns': 0}
    
    def has_valid_chess_pieces(piece):
        """A function that examines the argument piece and adds to the piece_counter dictionary, then checks if the number of pieces is valid."""
        
        # Check which player the piece belongs to
        if piece.startswith('b-'):
            player = 'b'
        elif piece.startswith('w-'):
            player = 'w'
        else:
            print(f'{coordinate} was empty.')
            return # stop running the function if the coordinate is empty
        
        # Add to the piece_counter dictionary depending on the player and type of chess piece
        # Checks if each player has exactly one king, at most 16 pieces and at most 8 pawns
        if piece.startswith(player):
            piece_counter[player + '-pieces'] += 1
            if piece_counter[player + '-pieces'] > 16:
                print(f'{player.capitalize()} has more than 16 pieces.')
                return False
            if chess_piece == player + '-king':
                piece_counter[piece] += 1
                if piece_counter[piece] != 1:
                    print(f'{player.capitalize()} does not have a king.')
                    return False
            elif chess_piece == player + '-pawn':
                piece_counter[player + '-pawns'] += 1
                if piece_counter[player + '-pawns'] > 8:
                    print(f'{player.capitalize()} has more than 8 pawns.')
                    return False
                
    # Check the validity of every coordinate in the dictionary
    for coordinate, chess_piece in board.items():
        if coordinate not in valid_coordinates:
            return False
        
        # Run a function to record the chess piece found on each coordinate
        if has_valid_chess_pieces(chess_piece) == False:
            return False
        
    print(piece_counter)
    return True  # Returns True if none of the invalid if conditions were triggered
        
print(is_valid_chess_board(chess_board))