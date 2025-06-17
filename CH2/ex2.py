sum = 0
n = int(input("Enter a natural number: "))

for i in range(1, n + 1):
    print("The current number is:", i)
    for j in range(1, n + 1):
        sum = sum + 1
    print("The current number is:", j)
    print("The sum is:", sum)

# 在這段程式碼中，我們使用了兩個嵌套的 for 迴圈。
# 關鍵在於，這個內層迴圈是在外層迴圈的每一次迭代中都會執行。
# i = 1 時，內層迴圈 j 從 1 到 n 執行一次。
# i = 2 時，內層迴圈 j 從 1 到 n 執行一次。
# sum = 外層迴圈執行次數 × 內層迴圈執行次數
# O(n^2) 的時間複雜度。