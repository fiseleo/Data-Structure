import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False 

x = np.linspace(1, 10, 100)


y1 = np.log2(x)          # O(log n)

y2 = x                   # O(n)

y3 = x * np.log2(x)      # O(n log n)

y4 = x**2                # O(n²)
y5 = np.power(2, x)      # O(2ⁿ)

plt.plot(x, y1, label='O($\log_2 n$)') # log_{2} n
plt.plot(x, y2, label='O($n$)')
plt.plot(x, y3, label='O($n \log n$)')
plt.plot(x, y4, label='O($n^2$)')      # n^2
plt.plot(x, y5, label='O($2^n$)')      # 2^n

# --- 圖表設定 ---
# 設定 y 軸為對數尺度，這樣才能同時看清楚所有函數的曲線
plt.yscale('log')


plt.xlim(1, 10)
plt.ylim(1, 10**3) 


plt.xlabel('n (輸入規模)')
plt.ylabel('操作次數 (對數尺度)')
plt.title('各種時間複雜度的成長趨勢比較')

# 顯示圖例與格線
plt.legend()
plt.grid(True, which="both", ls="--")


plt.show()