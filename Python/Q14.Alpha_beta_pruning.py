def alphabeta(position, depth, alpha, beta, maximizing_player):
    if depth == 0 or game_over(position):
        return evaluate(position)
    
    if maximizing_player:
        value = float('-inf')
        for child in get_children(position):
            value = max(value, alphabeta(child, depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                break  # Beta cutoff
        return value
    else:
        value = float('inf')
        for child in get_children(position):
            value = min(value, alphabeta(child, depth-1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break  # Alpha cutoff
        return value

def find_best_move_ab(board):
    best_val = float('-inf')
    best_move = None
    alpha = float('-inf')
    beta = float('inf')
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                move_val = alphabeta(board, 3, alpha, beta, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
                alpha = max(alpha, best_val)
    return best_move

# Helper functions for Tic Tac Toe
def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

def is_draw(board):
    if check_winner(board) is not None:
        return False
    return all(cell != " " for row in board for cell in row)

def game_over(board):
    return check_winner(board) is not None or is_draw(board)

def evaluate(board):
    winner = check_winner(board)
    if winner == "X":
        return 1
    elif winner == "O":
        return -1
    return 0

def get_children(board):
    children = []
    current_player = "X" if sum(cell == " " for row in board for cell in row) % 2 == 1 else "O"
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                new_board = [row.copy() for row in board]
                new_board[i][j] = current_player
                children.append(new_board)
    return children

# Example usage
if __name__ == "__main__":
    board = [
        ["X", "O", " "],
        [" ", "X", " "],
        [" ", " ", "O"]
    ]
    print("Current board:")
    for row in board:
        print(row)
    move = find_best_move_ab(board)
    print(f"Best move with Alpha-Beta: {move}")