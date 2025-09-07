import requests

# 目前程式版本
__version__ = "1.2.0"

# GitHub repo 資訊
OWNER = "ChinYi-Chiu"
REPO = "smartbackup"

def check_update():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/releases/latest"
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        latest = r.json()["tag_name"].lstrip("v")  # e.g. "v1.2.0" → "1.2.0"

        if latest != __version__:
            print(f"⚠️ 偵測到新版本 {latest}（目前 {__version__}）")
            print(f"下載位置: {r.json()['html_url']}")
        else:
            print("✅ 已經是最新版本")
    except Exception as e:
        print(f"❌ 更新檢查失敗: {e}")

if __name__ == "__main__":
    check_update()
