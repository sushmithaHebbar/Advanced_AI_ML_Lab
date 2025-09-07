<<<<<<< HEAD
import random

def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    print("\nCurrent Board:")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)
    print()

def check_winner(board, player):
    """Checks if the current player has won."""
    # Check rows and cols
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # row
            return True
        if all(board[j][i] == player for j in range(3)):  # col
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    """Checks if the board is full (a draw)."""
    return all(cell != " " for row in board for cell in row)

def get_player_move(board):
    """Gets the player's move (1–9)."""
    while True:
        try:
            move = int(input("Choose a position (1–9): "))
            if move < 1 or move > 9:
                print("Invalid input. Choose a number between 1 and 9.")
                continue

            row, col = divmod(move - 1, 3)
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            return row, col
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_ai_move(board):
    """Simple AI: picks a random empty spot."""
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(empty_cells)

def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game."""
    print("Welcome to Tic-Tac-Toe!")
    print("Board positions are numbered as follows:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9\n")

    mode = input("Do you want to play against another Player (P) or Computer (C)? ").lower().strip()

    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"

        while True:
            print_board(board)

            if mode == "c" and current_player == "O":
                print("Computer's turn...")
                row, col = get_ai_move(board)
            else:
                print(f"Player {current_player}'s turn")
                row, col = get_player_move(board)

            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"🎉 Player {current_player} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            # Switch player
            current_player = "O" if current_player == "X" else "X"

        # Replay option
        replay = input("Do you want to play again? (y/n): ").lower().strip()
        if replay != "y":
            print("Thanks for playing Tic-Tac-Toe! ")
            break

if __name__ == "__main__":
    tic_tac_toe()
=======
import random

def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    print("\nCurrent Board:")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)
    print()

def check_winner(board, player):
    """Checks if the current player has won."""
    # Check rows and cols
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # row
            return True
        if all(board[j][i] == player for j in range(3)):  # col
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    """Checks if the board is full (a draw)."""
    return all(cell != " " for row in board for cell in row)

def get_player_move(board):
    """Gets the player's move (1–9)."""
    while True:
        try:
            move = int(input("Choose a position (1–9): "))
            if move < 1 or move > 9:
                print("Invalid input. Choose a number between 1 and 9.")
                continue

            row, col = divmod(move - 1, 3)
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            return row, col
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_ai_move(board):
    """Simple AI: picks a random empty spot."""
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(empty_cells)

def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game."""
    print("Welcome to Tic-Tac-Toe!")
    print("Board positions are numbered as follows:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9\n")

    mode = input("Do you want to play against another Player (P) or Computer (C)? ").lower().strip()

    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"

        while True:
            print_board(board)

            if mode == "c" and current_player == "O":
                print("Computer's turn...")
                row, col = get_ai_move(board)
            else:
                print(f"Player {current_player}'s turn")
                row, col = get_player_move(board)

            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"🎉 Player {current_player} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            # Switch player
            current_player = "O" if current_player == "X" else "X"

        # Replay option
        replay = input("Do you want to play again? (y/n): ").lower().strip()
        if replay != "y":
            print("Thanks for playing Tic-Tac-Toe! ")
            break

if __name__ == "__main__":
    tic_tac_toe()
>>>>>>> 7e01e2e388143c3aeecd62e0b9083e0dcdc87b2e
