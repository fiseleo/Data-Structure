# Set
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7, 8}
# 集合的基本操作
print(f"A: {A}")
print(f"B: {B}")
# 集合的聯集
C = A | B  # 或者使用 A.union(B)
print(f"A ∪ B: {C}")
# 集合的交集
D = A & B  # 或者使用 A.intersection(B)
print(f"A ∩ B: {D}")
# 集合的差集
E = A - B  # 或者使用 A.difference(B)
print(f"A - B: {E}")
F = B - A  # 或者使用 B.difference(A)
print(f"B - A: {F}")

s1 = {"a", "b", "c"}  
s2 = {"a", "b"}
print(s1.issubset(s2))  # 檢查 s1 是否為 s2 的子集 False
print(s1.issuperset(s2))  # 檢查 s1 是否為 s2 的超集 True