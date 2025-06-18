list1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
n = int(input("請輸入一個數字: "))
if n < 1 or n > 26:
    print("請輸入介於 1 到 26 之間的數字。")
else:
    new_list = list1[0:n]
    print("前", n, "個字母是:", new_list)