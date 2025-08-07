from datetime import datetime
from task_pool import choose_task_phrase
from wechat_push import send_wechat

def main():
    today = datetime.now().strftime("%Y-%m-%d")
    task, phrase = choose_task_phrase()
    title = "🐯 橙导上线啦！"
    desp = (
        f"📅 {today}\n\n"
        f"{phrase}\n\n"
        f"👉 今日任务：**{task}**\n\n"
        f"💪 干一点是一点，干了再说！"
    )
    send_wechat(title, desp)

if __name__ == "__main__":
    main()
