# n - Queen's Problem

def isSafe(board, row, col):
    n = len(board)
    # 直行檢查 (Column Check)
    # 檢查在同一列上是否有皇后
    # 如果在 row 之前的行中有皇后放在 col 列，則返回 False

    for i in range(row):
        if board[i] == col:
            return False
        

    # 對角線檢查 (Diagonal Checks)
    # 檢查左上對角線
    # 檢查右上對角線

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < n:
        if board[i] == j:
            return False
        i -= 1
        j += 1
    return True

def solve_n_queens(board, row):
    n = len(board)
    # 如果已經放置了所有的皇后，則返回 True
    if row == n:
        return True
    
    for col in range(n):
        if isSafe(board, row, col):
            board[row] = col #「在棋盤的第 row 列，我們決定將皇后放在第 col 行/欄 上。」
            if solve_n_queens(board, row + 1):
                # 「在目前的第 row 列 成功放置皇后後，向下移動到下一 列 (row + 1)，繼續求解。」
                return True
            # 如果放置失敗，則回溯
            board[row] = -1
    return False

def n_queens(n):
    board = [-1] * n  # 初始化棋盤，-1表示沒有放置皇后
    # 嘗試解決 N 皇后問題
    if solve_n_queens(board, 0):
        for i in range(n):
            row_str = ""
            for j in range(n): # 列印棋盤
                if board[i] == j:
                    row_str += "Q " # Q表示有皇后
                else:
                    row_str += ". " # 空格表示沒有皇后
            print(row_str)
    else:
        print("No solution exists for", n, "queens.")
    
print("N-Queens Problem")
n = eval(input("Enter the number of queens: "))
n_queens(n)

# 在一行中，嘗試將皇后放在某一格。
# ：如果這個位置是安全的（不會被其他皇后攻擊），就跳到下一行，繼續為下一行的皇后找位置。
# 如果在某一整行都找不到任何安全的位置可以放皇后，就表示上一行的皇后位置錯了，導致後面「無路可走」。這時，程式會退回到上一行，將皇后從原來的位置拿起，然後嘗試放在該行的下一個位置。
# 根據求解器的回傳值（True 或 False）來決定是列印找到的解，還是宣告無解。
#終止條件: if row == n 意思是，如果我們已經成功放好了第 0 到 n-1 行的皇后，表示找到了一組解！函式返回 True，這個 True 會像漣漪一樣傳回給所有上層的呼叫者。
#  遍歷選擇: for col in range(n): 對於目前的 row，我們嘗試將皇后放在每一個可能的 col 上。
# 檢查有效性: if isSafe(...) 呼叫輔助函式，檢查 (row, col) 這個位置是否會被之前放好的皇后攻擊。
# 如果安全，就更新棋盤 board[row] = col，代表「暫時」將皇后放在這裡。
# solve_n_queens(board, row + 1) 這是最關鍵的一步。我們基於目前的決定，去解決下一行的問題。如果這個呼叫最終返回了 True，表示我們的決定是正確的，可以直接將 True 返回。
# 如果 (E) 返回了 False，代表剛才把皇后放在 (row, col) 是個錯誤的決定，它導致了後面的「死路」。因此，我們必須撤銷這個選擇 (board[row] = -1)，然後 for 迴圈會繼續，嘗試將皇后放在 row 的下一個 col 位置。
# 宣告失敗: 如果 for 迴圈跑完了（所有 col 都試過了），還是沒有找到一個可行的位置，代表在這一層無解。函式返回 False 給上一層，觸發上一層的回溯。
# isSafe(board, row, col): 規則檢查器
# 這個函式的作用很單純：判斷在 (row, col) 放皇后，是否違反 N 皇后的規則。