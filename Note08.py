# Requests

import requests

# 1. 發送 GET 請求：使用 requests.get()
# 發送請求到一個免費的 JSON 測試 API
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

# 檢查 HTTP 狀態碼：response.status_code
print("1. HTTP 狀態碼：")
print(response.status_code)

# 2. 解析 JSON 回應：使用 response.json()
# 將回應內容解析為 Python 字典
if response.status_code == 200:  # 確保請求成功
    data = response.json()
    print("\n2. JSON 回應內容：")
    print(data)
else:
    print("\n無法取得 JSON 回應")

# 3. 提取特定欄位：使用字典操作
# 從 JSON 回應中提取特定欄位
if "title" in data:
    title = data["title"]
    print("\n3. 提取的欄位 'title'：")
    print(title)

# 4. 發送 POST 請求：使用 requests.post()
# 發送一個包含 JSON 資料的 POST 請求
post_url = "https://jsonplaceholder.typicode.com/posts"
post_data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
post_response = requests.post(post_url, json=post_data)

# 檢查 POST 回應
print("\n4. POST 請求結果：")
print(f"HTTP 狀態碼: {post_response.status_code}")
print("回應內容：")
print(post_response.json())

# 5. 自訂請求標頭：使用 headers
# 發送帶有自訂標頭的 GET 請求
headers = {
    "User-Agent": "Python-Requests/4.0"
}
custom_response = requests.get(url, headers=headers)
print("\n5. 自訂標頭的請求：")
print(f"HTTP 狀態碼: {custom_response.status_code}")

# 6. 提取回應標頭：使用 response.headers
# 查看回應中的標頭資訊
response_headers = custom_response.headers
print("\n6. 回應標頭：")
print(response_headers)

# 7. 使用 response.text 提取純文字內容
# 提取純文字內容（未處理的回應內容）
response_text = response.text
print("\n7. 回應的純文字內容：")
print(response_text[:100])  # 只顯示前 100 個字元

# 8. 錯誤處理：使用 try-except
# 處理請求時可能發生的例外
invalid_url = "https://invalid.url"
try:
    invalid_response = requests.get(invalid_url)
    print("\n8. 錯誤處理範例：")
    print(invalid_response.status_code)
except requests.exceptions.RequestException as e:
    print("\n無法連線到指定網址：")
    print(str(e))

# 9. 發送帶有查詢參數的 GET 請求：使用 params
# 發送一個帶有查詢參數的 GET 請求
query_url = "https://jsonplaceholder.typicode.com/posts"
params = {
    "userId": 1
}
query_response = requests.get(query_url, params=params)
print("\n9. 帶有查詢參數的 GET 請求：")
print(query_response.url)  # 查看完整的請求 URL
print(query_response.json()[:2])  # 顯示前兩筆資料

# 10. 檢查內容類型：使用 response.headers["Content-Type"]
# 檢查回應的內容類型
content_type = response.headers.get("Content-Type", "未知")
print("\n10. 回應的內容類型：")
print(content_type)