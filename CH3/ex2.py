tuple1 = (1, 2, 3, 4, 5)
tuple2 = tuple(i for i in range(1, 6))  # 使用生成器表達式創建元組
print(tuple1)
print(tuple2)
tuple3 = tuple1 + tuple2  # 合併兩個元組
print(tuple3)
print(tuple1[1])  # 訪問元組的第2個元素
print(tuple1[-2])  # 訪問元組的倒數第2個元素


# Tuple的不可變性

#try:
#    tuple1[0] = 10  # 嘗試修改元組的第一個元素
#except TypeError as e:
#    print(f"錯誤: {e}")

# Tuple的不可變性確保了數據的完整性和安全性

a = tuple1.count(1)  # 計算元組中1出現的次數
b = tuple1.index(3)  # 查找元組中3的索引位置
print(f"元組1中1出現的次數: {a}")
print(f"元組1中3的索引位置: {b}")