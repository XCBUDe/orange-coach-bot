import requests
import os

SENDKEY = os.getenv("SENDKEY", "SCT291864TypJsxNKmXlDUq9y5EkgEsOtW")  # 这里换成你的 SendKey

def send_wechat(title, desp):
    url = f"https://sctapi.ftqq.com/{SENDKEY}.send"
    data = {"title": title, "desp": desp}
    res = requests.post(url, data=data)
    print("Server酱返回：", res.text)
