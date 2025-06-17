sum = 0
n = int(input("Enter a natural number: "))
for i in range(1, n + 1):
    print("The current number is:", i)
    for j in range(1, i + 1):
        sum = sum +1
    print("The current number is:", j)
    print("The sum is:", sum)
    


# 在這段程式碼中，我們使用了兩個嵌套的 for 迴圈。
# 外層迴圈遍歷從 1 到 n 的所有自然數，內層迴圈遍歷從 1 到當前外層迴圈的數字 i。
# 每次內層迴圈執行時，我們將 sum 變數加 1，最終計算出從 1 到 n 的總和。
# 外層迴圈先執行。 
# 可以把巢狀迴圈想像成時鐘的時針 (外層) 和 分針 (內層)：
# 時針 (外層迴圈) 先走一格。
# 然後分針 (內層迴圈) 必須完整地走完一整圈。
# 分針走完後，時針 (外層迴圈) 才再走下一格。
# 分針走完後，時針 (外層迴圈) 才再走下一格。
# O(n^2) 的時間複雜度。

# Python 的 range(start, stop) 函數會產生一個從 start 開始，到 stop - 1 結束的整數序列。