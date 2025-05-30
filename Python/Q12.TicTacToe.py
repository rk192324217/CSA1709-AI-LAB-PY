import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def ai_move(board, ai_char, player_char):
    # Check for winning move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = ai_char
                if check_winner(board) == ai_char:
                    return i, j
                board[i][j] = " "
    
    # Block player's winning move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = player_char
                if check_winner(board) == player_char:
                    board[i][j] = ai_char
                    return i, j
                board[i][j] = " "
    
    # Take center if available
    if board[1][1] == " ":
        return 1, 1
    
    # Choose random corner
    corners = [(0,0), (0,2), (2,0), (2,2)]
    random.shuffle(corners)
    for i, j in corners:
        if board[i][j] == " ":
            return i, j
    
    # Choose any available cell
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return i, j

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_char = "X"
    ai_char = "O"
    
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    
    while True:
        # Player move
        while True:
            try:
                row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                    break
                print("Invalid move! Try again.")
            except:
                print("Invalid input! Enter two numbers (0-2) separated by space.")
        
        board[row][col] = player_char
        print_board(board)
        
        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break
        
        # AI move
        print("AI's turn...")
        ai_row, ai_col = ai_move(board, ai_char, player_char)
        board[ai_row][ai_col] = ai_char
        print_board(board)
        
        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()