import random
n = input("請輸入一個正整數 n: ")
n = int(n)
list = []
for i in range(n):
    list.append(random.randint(1, 100))  # 隨機生成1到100之間的整數
print("生成的列表:", list)
