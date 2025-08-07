import os
import requests

SENDKEY = os.getenv("SENDKEY")

def send_wechat(title: str, desp: str):
    url = f"https://sctapi.ftqq.com/{SENDKEY}.send"
    data = {"title": title, "desp": desp}
    resp = requests.post(url, data=data, timeout=10)
    resp.raise_for_status()
    return resp.json()
