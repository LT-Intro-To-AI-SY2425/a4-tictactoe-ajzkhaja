# NOTE: Until you fill in the TTTBoard class mypy is going to give you multiple errors
# talking about unimplemented class attributes, don't worry about this as you're working

class TTTBoard:
    """A Tic Tac Toe board representation.

    Attributes:
        board: A list containing '*' for empty spots, 'X' for player X's moves,
               and 'O' for player O's moves.
    """
    
    def __init__(self) -> None:
        """Initialize a 3x3 tic tac toe board with empty spots."""
        self.board = ['*'] * 9

    def __str__(self) -> str:
        """Return a string representation of the board."""
        return f"{self.board[0]} {self.board[1]} {self.board[2]}\n" \
               f"{self.board[3]} {self.board[4]} {self.board[5]}\n" \
               f"{self.board[6]} {self.board[7]} {self.board[8]}"

    def make_move(self, player: str, pos: int) -> bool:
        """Place a move for the specified player at the given position.

        Args:
            player: Either 'X' or 'O'.
            pos: An integer position from 0 to 8.

        Returns:
            True if the move was successful, False otherwise.
        """
        if 0 <= pos < 9 and self.board[pos] == '*':
            self.board[pos] = player
            return True
        return False

    def has_won(self, player: str) -> bool:
        """Check if the specified player has won.

        Args:
            player: Either 'X' or 'O'.

        Returns:
            True if the player has won, False otherwise.
        """
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]               # Diagonals
        ]
        return any(all(self.board[pos] == player for pos in combo) for combo in winning_combinations)

    def game_over(self) -> bool:
        """Check if the game is over due to a win or a full board.

        Returns:
            True if the game is over, False otherwise.
        """
        return self.has_won("X") or self.has_won("O") or '*' not in self.board

    def clear(self) -> None:
        """Reset the board for a new game."""
        self.board = ['*'] * 9


def play_tic_tac_toe() -> None:
    
    
    def is_integer(value: str) -> bool:
        """Check if a string can be converted to an integer.

        Args:
            value: The string to check.

        Returns:
            True if the string is an integer, False otherwise.
        """
        return value.isdigit()     

    board = TTTBoard()          
    players = ["X", "O"]
    turn = 0

    while not board.game_over():
        print(board)
        move_input = input(f"Player {players[turn]}, enter your move (0-8): ")

        if not is_integer(move_input):
            raise ValueError(f"Invalid input: {move_input}. Please enter an integer between 0 and 8.")

        move = int(move_input)

        if board.make_move(players[turn], move):
            turn = 1 - turn  # Switch turns

    print(f"\nGame over!\n\n{board}")                 
    if board.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif board.has_won(players[1]):        
        print(f"{players[1]} wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    # here are some tests. These are not at all exhaustive tests. You will DEFINITELY
    # need to write some more tests to make sure that your TTTBoard class is behaving
    # properly.
    brd = TTTBoard()
    brd.make_move("X", 8)
    brd.make_move("O", 7)

    assert brd.game_over() == False

    brd.make_move("X", 5)
    brd.make_move("O", 6)
    brd.make_move("X", 2)

    assert brd.has_won("X") == True
    assert brd.has_won("O") == False
    assert brd.game_over() == True

    brd.clear()

    assert brd.game_over() == False

    brd.make_move("O", 3)
    brd.make_move("O", 4)
    brd.make_move("O", 5)

    assert brd.has_won("X") == False
    assert brd.has_won("O") == True
    assert brd.game_over() == True

    print("All tests passed!")

    # uncomment to play!
    play_tic_tac_toe()