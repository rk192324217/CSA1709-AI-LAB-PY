def minimax(position, depth, maximizing_player):
    if depth == 0 or game_over(position):
        return evaluate(position)
    
    if maximizing_player:
        max_eval = float('-inf')
        for child in get_children(position):
            eval = minimax(child, depth-1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for child in get_children(position):
            eval = minimax(child, depth-1, True)
            min_eval = min(min_eval, eval)
        return min_eval

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

def find_best_move(board):
    best_val = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                move_val = minimax(board, 3, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

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
    move = find_best_move(board)
    print(f"Best move for X: {move}")