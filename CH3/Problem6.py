Dict = {"H" : "紅心" , "S" : "黑桃", "D" : "方塊", "C" : "梅花"} # HSDC
Dict2 = {"A" : "A", "2" : "2", "3" : "3", "4" : "4", "5" : "5", "6" : "6", "7" : "7", "8" : "8", "9" : "9", "T" : "T", "J" : "J", "Q" : "Q", "K" : "K"} # A23456789TJQK
fivecard = input("請輸入五張牌(例如: H2 S3 D4 C5 H6): ").upper().split()  # 將輸入轉為大寫並分割成列表
if len(fivecard) != 5:
    print("請輸入五張牌。")
else:
    for card in fivecard:
        if len(card) != 2 or card[0] not in Dict or card[1] not in Dict2: 
            # 檢查牌的格式是否正確
            # 檢查 card 的長度是否不等於 2。如果 card 的長度不是 2，條件成立。
            # 檢查 card 的第一個元素 (card[0]) 是否不在 Dict 中。如果 card[0] 不在 Dict 中，條件成立。
            # 檢查 card 的第二個元素 (card[1]) 是否不在 Dict2 中。如果 card[1] 不在 Dict2 中，條件成立。
            print(f"牌 {card} 格式錯誤，請輸入正確的牌。")
            break
    else:
        suits = [Dict[card[0]] for card in fivecard]
        ranks = [Dict2[card[1]] for card in fivecard]
        cards = [f"{suit}{rank}" for suit, rank in zip(suits, ranks)]
        # zip(suits, numbers)  將花色 (suits) 和數字 (numbers) 配對在一起。
        # f"{suit}{number}" 使用格式化字串將花色和數字結合成一個字串。
        # 輸出結果
        print("五張牌:", " ".join(cards))
        # 將所有牌用空格連接成一個字串，方便輸出。
