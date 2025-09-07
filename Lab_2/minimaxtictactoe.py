import math  # Import math module for using -infinity

# Initialize the board with 9 empty spaces (list of 9 strings, each " ")
b = [" "] * 9  

# All possible winning combinations (rows, columns, diagonals)
w = [
    [0, 1, 2],  # Top row
    [3, 4, 5],  # Middle row
    [6, 7, 8],  # Bottom row
    [0, 3, 6],  # Left column
    [1, 4, 7],  # Middle column
    [2, 5, 8],  # Right column
    [0, 4, 8],  # Left diagonal
    [2, 4, 6]   # Right diagonal
]

# Function to display the current board
def show():
    # Join each row with "|" and print them as a 3x3 board
    print("\n".join(["|".join(b[i:i+3]) for i in range(0, 9, 3)]))

# Function to check if player p ("X" or "O") has won
def win(p):
    # Return True if any winning combination is filled with p
    return any(all(b[i] == p for i in c) for c in w)

# Function to check if board is full (draw condition)
def full():
    # If no empty spaces remain, return True
    return " " not in b

# Minimax algorithm for optimal move calculation
def minimax(p):
    # If computer "O" wins, return positive score
    if win("O"): return 1
    # If human "X" wins, return negative score
    if win("X"): return -1
    # If board is full (draw), return 0
    if full(): return 0

    scores = []  # Store possible outcomes for all moves

    # Loop through all board positions
    for i in range(9):
        if b[i] == " ":  # If cell is empty
            b[i] = p  # Place player's move temporarily
            # Recursively call minimax for the opponent
            scores.append(minimax("X" if p == "O" else "O"))
            b[i] = " "  # Undo move (backtrack)

    # If it's "O"’s turn (computer), maximize score
    # If it's "X"’s turn (human), minimize score
    return max(scores) if p == "O" else min(scores)

# Function to find the best move for computer "O"
def best():
    m, s = -1, -math.inf  # Initialize move and best score (-infinity)
    for i in range(9):  # Check all cells
        if b[i] == " ":  # If cell is empty
            b[i] = "O"  # Try placing "O"
            sc = minimax("X")  # Evaluate move by running minimax for "X"
            b[i] = " "  # Undo move
            if sc > s:  # If score is better than current best
                s, m = sc, i  # Update best score and best move
    return m  # Return the best move index

# Main game loop (human vs computer)
def play():
    print("You: X, Computer: O")  # Show roles
    show()  # Print initial empty board

    while True:  # Keep playing until win or draw
        h = int(input("Move (1-9): ")) - 1  # Human move (1-9 → 0-8 index)
        if b[h] != " ":  # Check if cell is already filled
            print("Invalid")  # If yes, warn user
            continue  # Ask again

        b[h] = "X"  # Place human move
        if win("X"):  # Check if human wins
            show()
            print("You win!")
            break

        if full():  # If board is full, it's a draw
            show()
            print("Draw!")
            break

        c = best()  # Computer chooses best move
        b[c] = "O"  # Place computer move
        print("\nComputer:", c + 1)  # Show computer move (1-9)
        show()  # Print updated board

        if win("O"):  # Check if computer wins
            print("Computer wins!")
            break

        if full():  # If board full after computer move → Draw
            print("Draw!")
            break
play()