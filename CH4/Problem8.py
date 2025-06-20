#Sudoku

def isValid(board, row, col, num):
    if num in board[row]:
        return False
    
    if num in [board[i][col] for i in range(9)]:
        return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True
    
    row, col = empty
    for num in range(1, 10):
        if isValid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False



def print_board(board):
    for row in board:
        for num in row:
            print(str(num) if num != 0 else '_', end=' ')
        print()


sudoku_board = [
    [0, 2, 0, 1, 4, 0, 9, 7, 0],
    [8, 0, 0, 0, 5, 9, 0, 0, 4],
    [0, 4, 0, 0, 0, 6, 0, 0, 0],
    [5, 7, 0, 9, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 6, 7, 0, 3, 9],
    [0, 9, 0, 0, 0, 0, 7, 0, 8],
    [0, 0, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 0, 8, 2, 4, 3, 9, 5],
    [4, 0 ,2 ,0 ,0 ,0 ,0 ,8 ,0]
]
print("Sudoku Board:")
print_board(sudoku_board)
if solve_sudoku(sudoku_board):
    print("\nSolved Sudoku Board:")
    print_board(sudoku_board)
else:
    print("No solution exists for the given Sudoku puzzle.")
