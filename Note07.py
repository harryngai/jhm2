# Matplotlib

import matplotlib.pyplot as plt

# 1. 繪製折線圖
# 範例資料
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [200, 300, 400, 350, 500]

# 繪製折線圖
plt.plot(months, sales, marker='o', label="Sales")
plt.title("Monthly Sales")  # 圖表標題
plt.xlabel("Month")         # X 軸標籤
plt.ylabel("Sales ($)")     # Y 軸標籤
plt.legend()                # 顯示圖例
plt.grid(True)              # 顯示網格
plt.show()

# 2. 繪製長條圖
# 範例資料
products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor']
revenue = [5000, 800, 1200, 3000]

# 繪製長條圖
plt.bar(products, revenue, color='skyblue')
plt.title("Product Revenue")  # 圖表標題
plt.xlabel("Product")         # X 軸標籤
plt.ylabel("Revenue ($)")     # Y 軸標籤
plt.show()

# 3. 繪製圓餅圖
# 範例資料
categories = ['Electronics', 'Clothing', 'Food']
percentages = [40, 35, 25]

# 繪製圓餅圖
plt.pie(percentages, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title("Revenue Distribution")  # 圖表標題
plt.show()

# 4. 同時繪製多個子圖
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 子圖 1: 折線圖
axes[0].plot(months, sales, marker='o', color='green')
axes[0].set_title("Monthly Sales")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("Sales ($)")
axes[0].grid(True)

# 子圖 2: 長條圖
axes[1].bar(products, revenue, color='orange')
axes[1].set_title("Product Revenue")
axes[1].set_xlabel("Product")
axes[1].set_ylabel("Revenue ($)")

plt.tight_layout()  # 自動調整子圖間距
plt.show()

# 5. 儲存圖表到檔案
# 儲存折線圖為圖片
plt.plot(months, sales, marker='o', label="Sales")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.legend()
plt.savefig("monthly_sales.png")  # 儲存到檔案
print("圖表已儲存為 monthly_sales.png")