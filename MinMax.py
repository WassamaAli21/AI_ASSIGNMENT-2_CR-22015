import math

# Initialize the board
board = [' ' for _ in range(9)]

# Print the board
def print_board():
    for i in range(3):
        print('|'.join(board[i*3:(i+1)*3]))
        if i < 2:
            print('-' * 5)

# Check for a winner
def check_winner(brd, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(brd[i] == player for i in cond) for cond in win_conditions)

# Check for tie
def is_full(brd):
    return all(spot != ' ' for spot in brd)

# Minimax algorithm
def minimax(brd, depth, is_maximizing):
    if check_winner(brd, 'O'):
        return 1
    if check_winner(brd, 'X'):
        return -1
    if is_full(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'O'
                score = minimax(brd, depth + 1, False)
                brd[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'X'
                score = minimax(brd, depth + 1, True)
                brd[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Get the best move for AI
def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Main game loop
def play_game():
    print("Tic-Tac-Toe (You = X, AI = O)")
    print_board()

    while True:
        # Player move
        move = int(input("Enter your move (0-8): "))
        if board[move] != ' ':
            print("Invalid move, try again.")
            continue
        board[move] = 'X'
        print_board()

        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        # AI move
        ai_move = best_move()
        board[ai_move] = 'O'
        print("\nAI played:")
        print_board()

        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

# Run the game
play_game()