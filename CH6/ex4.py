# Donble-Ended Queue

from collections import deque

d = deque()
d.append(1)  # 在右端加入元素
d.append(2)  # 在右端加入元素
d.append(3)  # 在右端加入元素
d.appendleft(0)  # 在左端加入元素
d.appendleft(-1)  # 在左端加入元素
print("Deque after additions:", d)

d.pop()  # 從右端移除元素
print("Deque after popping from right:", d)

d.popleft()  # 從左端移除元素
print("Deque after popping from left:", d)

print("Current length of deque:", len(d))
print("leftmost element:", d[0])  # 左端元素
print("rightmost element:", d[-1])  # 右端元素