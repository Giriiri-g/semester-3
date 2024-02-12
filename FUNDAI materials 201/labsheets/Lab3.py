from logic import Square, Mark

X, O, BLANK = 'X', 'O', ' '

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == BLANK

def is_game_over(board):
    return is_winning(board, X) or is_winning(board, O) or all(mark != BLANK for row in board for mark in row)

# Function to determine if a player has won the game
# Function to determine if a player has won the game
def is_winning(board, player):
    # Define winning combinations
    winning_combinations = [
        # Rows
        [(1, 1), (1, 2), (1, 3)],
        [(2, 1), (2, 2), (2, 3)],
        [(3, 1), (3, 2), (3, 3)],
        # Columns
        [(1, 1), (2, 1), (3, 1)],
        [(1, 2), (2, 2), (3, 2)],
        [(1, 3), (2, 3), (3, 3)],
        # Diagonals
        [(1, 1), (2, 2), (3, 3)],
        [(1, 3), (2, 2), (3, 1)]
    ]

    for combination in winning_combinations:
        marks = [board[row - 1][col - 1] for row, col in combination]
        if marks == [player] * 3:
            return True  # Return True immediately when a winning combination is found
    return False

def play_game():
    board = [[BLANK] * 3 for _ in range(3)]
    current_player = X

    # Print the initial board before the first input
    print("Initial Board:")
    print_board(board)

    # Inside the main game loop
    while not is_game_over(board):
        row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
        col = int(input(f"Player {current_player}, enter column (1-3): ")) - 1

        if is_valid_move(board, row, col):
            board[row][col] = current_player
            print("Updated Board:")
            print_board(board)  # Printed after the player makes a move
            if is_winning(board, current_player):
                print(f"Player {current_player} wins!")
                return
            current_player = O if current_player == X else X
        else:
            print("Invalid move. Try again.")

    print("It's a draw!")


play_game()
