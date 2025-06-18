import random
list1 = []
for i in range(50):
    list1.append(i)

print(list1)

list2 = [i for i in range(50)]
print(list2)

# 快速生成list

list3 = [random.randint(1, 100) for i in range(50)]
print(list3)
# 快速生成list，隨機數字範圍1到100，長度50

list4 = [[0 for j in range(5)] for i in range(5)] # 生成5x5的二維list，初始值為0
print(list4)

list5 = [1, 2, 3, 4]
list5.insert(1, 5)
print(list5)  # 在索引1的位置插入5，結果為 [1, 5, 2, 3, 4]