# 將英文設為 key，中文設為 value
Dict = {"Apples": "蘋果", "Bananas": "香蕉", "Oranges": "橘子" , "Grapes": "葡萄" , "Strawberries": "草莓", "Blueberries": "藍莓", "Lemons": "檸檬", "Peaches": "桃子", "Pears": "梨子", "Watermelons": "西瓜"}

# 在接收 input 後，立刻使用 .title() 來格式化字串
Values = input("請輸入水果英文名稱: ").title() 

if Values in Dict:
    print("對應的中文名稱是:", Dict[Values])
else:
    print("對不起，沒有找到對應的中文名稱。")
    # 提示時，也應該列出英文的 key
    print("請輸入以下水果英文名稱:", ", ".join(Dict.keys()))
    
    # 第二次輸入也需要格式化
    Values = input("請重新輸入水果英文名稱: ").title()
    if Values in Dict:
        print("對應的中文名稱是:", Dict[Values])
    else:
        print("仍然沒有找到對應的中文名稱。")