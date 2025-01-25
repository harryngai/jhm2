# API Key

import os
import json
from decouple import config  # 安裝方法：`pip install python-decouple`
from dotenv import load_dotenv  # 安裝方法：`pip install python-dotenv`
from cryptography.fernet import Fernet  # 安裝方法：`pip install cryptography`

# 1. 使用環境變數
def get_api_key_from_env():
    """從環境變數中取得 API 金鑰。"""
    api_key = os.getenv("API_KEY")
    if not api_key:
        # Linux/MacOS: export API_KEY="your_api_key_osenv"
        # Windows: set API_KEY=your_api_key_osenv
        raise ValueError("未找到 API 金鑰，請設定環境變數 API_KEY。")
    return api_key

# 2. 使用 .env 檔案
def get_api_key_from_dotenv():
    """從 .env 檔案中取得 API 金鑰。"""
    load_dotenv()  # 從 .env 檔案載入環境變數
    api_key = os.getenv("API_KEY_DOTENV")
    if not api_key:
        raise ValueError("未找到 API 金鑰，請檢查您的 .env 檔案。")
    return api_key

# 3. 使用設定檔（如 JSON）
def get_api_key_from_config():
    """從 JSON 設定檔案中取得 API 金鑰。"""
    try:
        with open("config.json", "r") as config_file:
            config = json.load(config_file)
            api_key = config.get("api_key")
            if not api_key:
                raise ValueError("未在 config.json 中找到 API 金鑰。")
            return api_key
    except FileNotFoundError:
        raise FileNotFoundError("未找到 config.json 設定檔案。")

# 4. 加密與解密設定檔案
def encrypt_config(input_file, output_file, key):
    """加密設定檔案。"""
    with open(input_file, "rb") as f:
        data = f.read()
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)
    with open(output_file, "wb") as f:
        f.write(encrypted_data)

def decrypt_config(encrypted_file, key):
    """解密設定檔案。"""
    with open(encrypted_file, "rb") as f:
        encrypted_data = f.read()
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data)
    return json.loads(decrypted_data)

# 範例
def main():
    # 1. 使用環境變數
    try:
        print("1. 從環境變數取得 API 金鑰：")
        api_key_env = get_api_key_from_env()
        print(f"API 金鑰：{api_key_env}")
    except ValueError as e:
        print(e)

    # 2. 使用 .env 檔案
    try:
        print("\n2. 從 .env 檔案取得 API 金鑰：")
        api_key_dotenv = get_api_key_from_dotenv()
        print(f"API 金鑰：{api_key_dotenv}")
    except ValueError as e:
        print(e)

    # 3. 使用設定檔
    try:
        print("\n3. 從設定檔取得 API 金鑰：")
        api_key_config = get_api_key_from_config()
        print(f"API 金鑰：{api_key_config}")
    except (ValueError, FileNotFoundError) as e:
        print(e)

    # 4. 加密與解密設定檔
    encrypted_file = "config_encrypted.json"
    plain_file = "config.json"

    # 檢查是否存在加密檔案
    if os.path.exists(encrypted_file):
        print("\n發現加密設定檔案，請輸入解密金鑰：")
        user_key = input("請輸入加密金鑰：").encode()  # 使用者輸入解密金鑰
        try:
            # 嘗試解密檔案
            decrypted_config = decrypt_config(encrypted_file, user_key)
            print("解密成功，設定內容如下：", decrypted_config)
            api_key = decrypted_config.get("api_key")
            print(f"從加密檔案取得的 API 金鑰：{api_key}")
        except Exception as e:
            print(f"解密失敗，請確認金鑰是否正確。錯誤：{e}")
    else:
        print("\n未找到加密設定檔案，將建立新的加密檔案：")
        # 生成新的加密金鑰（僅需生成一次，並安全保存）
        key = Fernet.generate_key()
        print(f"新加密金鑰（請安全保存）：{key.decode()}")

        # 檢查是否存在未加密的設定檔案
        if not os.path.exists(plain_file):
            print(f"未找到 {plain_file}，請建立包含 API 金鑰的設定檔。")
            # 建立一個範例設定檔
            example_config = {
                "api_key": "your_api_key_here",
                "database_url": "postgresql://user:password@localhost:5432/mydatabase",
                "debug": True
            }
            with open(plain_file, "w") as f:
                json.dump(example_config, f, indent=4)
            print(f"範例設定檔已建立為 {plain_file}，請修改內容後重新執行程式。")
            return

        # 加密設定檔案
        encrypt_config(plain_file, encrypted_file, key)
        print(f"成功加密設定檔案為 {encrypted_file}，原始檔案 {plain_file} 已加密。")
        print("請妥善保存加密金鑰以便未來解密。")

    # 提醒：確保敏感檔案如 `.env` 和 `config.json` 已加入 `.gitignore`。

if __name__ == "__main__":
    main()