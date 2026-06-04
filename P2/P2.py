# P2 Tic Tac Toe Algorithm

import math

# Initialize board
board = [' ' for _ in range(9)]

# Display board
def print_board():
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
    print()

# Check winner
def check_winner(player):
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]

    for combo in win_combinations:
        if all(board[pos] == player for pos in combo):
            return True
    return False

# Check draw
def is_draw():
    return ' ' not in board

# Minimax algorithm
def minimax(is_maximizing):

    if check_winner('O'):  # AI wins
        return 1

    if check_winner('X'):  # Human wins
        return -1

    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)

        return best_score

# AI move
def ai_move():

    best_score = -math.inf
    best_move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = 'O'

# Main game loop
def play_game():

    print("TIC-TAC-TOE (MINIMAX)")
    print("You are X")
    print("Positions:")
    print("0 | 1 | 2")
    print("3 | 4 | 5")
    print("6 | 7 | 8")

    while True:

        print_board()

        # Human move
        move = int(input("Enter position (0-8): "))

        if move < 0 or move > 8 or board[move] != ' ':
            print("Invalid move!")
            continue

        board[move] = 'X'

        if check_winner('X'):
            print_board()
            print("You Win!")
            break

        if is_draw():
            print_board()
            print("Match Draw!")
            break

        # AI move
        ai_move()

        if check_winner('O'):
            print_board()
            print("AI Wins!")
            break

        if is_draw():
            print_board()
            print("Match Draw!")
            break

# Run game
play_game()
