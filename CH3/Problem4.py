#Set
SetA = input("請輸入集合A的元素，以逗號分隔: ")
SetA = SetA.split(",")  # 將輸入的字符串分割成列表
SetA = set(SetA)  # 將列表轉換為集合
SetB = input("請輸入集合B的元素，以逗號分隔: ")
SetB = SetB.split(",")  # 將輸入的字符串分割成列表
SetB = set(SetB)  # 將列表轉換為集合

print("交集:", SetA & SetB)  # 集合的交集
print("聯集:", SetA | SetB)  # 集合的聯集