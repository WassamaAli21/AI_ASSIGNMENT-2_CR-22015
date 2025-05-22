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

# Check if board is full (draw)
def is_full(brd):
    return all(spot != ' ' for spot in brd)

# Minimax with Alpha-Beta Pruning
def minimax_ab(brd, depth, is_maximizing, alpha, beta):
    if check_winner(brd, 'O'):
        return 1
    if check_winner(brd, 'X'):
        return -1
    if is_full(brd):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'O'
                eval = minimax_ab(brd, depth + 1, False, alpha, beta)
                brd[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Beta cutoff
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'X'
                eval = minimax_ab(brd, depth + 1, True, alpha, beta)
                brd[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha cutoff
        return min_eval

# Best move using alpha-beta pruning
def best_move_ab():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax_ab(board, 0, False, -math.inf, math.inf)
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
        try:
            move = int(input("Enter your move (0-8): "))
            if board[move] != ' ':
                print("Invalid move, try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 0 and 8.")
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
        ai_move = best_move_ab()
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