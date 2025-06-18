#dictionary
dict1 = {'A': 1, 'B': 2, 'C': 3}
dict2 = {'D': 4, 'E': 5}

a = dict1['A']  # 訪問字典中的值
b = dict1.get('B')  # 使用 get 方法訪問字典中的值
print(f"dict1['A']: {a}")
print(f"dict1.get('B'): {b}")
dict1['C'] = 114514  # 修改字典中的值
print(f"修改後的 dict1: {dict1}")
dict1.update(dict2)  # 合併兩個字典
print(f"合併後的 dict1: {dict1}")
dict1.keys()  # 獲取字典的所有鍵
print(f"dict1 的所有鍵: {dict1.keys()}")