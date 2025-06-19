# Knight Tour Problem

def isSafe(board, row, col, n):
    return (row >= 0 and col >= 0 and row < n and col < n and \
            board[row][col] == -1)

def solve_knight_tour(board, row, col, count, move_x, move_y, n):
    if count == n * n + 1:
        return True
    
    for i in range(8):
        new_row = row + move_x[i]
        new_col = col + move_y[i]
        if isSafe(board, new_row, new_col, n):
            board[new_row][new_col] = count
            if solve_knight_tour(board, new_row, new_col, \
                                 count + 1, move_x, move_y , n):
                return True
            board[new_row][new_col] = -1
    return False

def knight_tour(n):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    
    board[0][0] = 1  # Start from the first cell
    if not solve_knight_tour(board, 0, 0, 2, move_x, move_y, n):
        print("No solution exists")
    else:
        print("Knight's Tour Solution:")
        print_board(board)


def print_board(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            print(f"{board[i][j]:3d}", end=" ")
        print()

print("Knight's Tour Problem")
n = int(input("Enter the size of the chessboard (n x n): "))
knight_tour(n)