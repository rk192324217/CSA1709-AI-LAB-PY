N = 8

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("\n")

def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j]:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j]:
            return False

    return True

def solve_n_queens(board, row=0):
    if row == N:
        print_board(board)
        return True  # Change to return False to print all solutions

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_n_queens(board, row + 1):
                return True  # Change to continue to find all solutions
            board[row][col] = 0  # Backtrack

    return False

# Driver code
if __name__ == "__main__":
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_n_queens(board):
        print("No solution exists.")
