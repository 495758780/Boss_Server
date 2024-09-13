import schedule
import time
import json
from datetime import datetime

def task():

    # 获取当前时间
    now = datetime.now()

    # 格式化当前时间为更友好的格式
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

    # 打印格式化后的时间
    print("当前时间是:", formatted_time)

    with open('user_info.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print('修改前的信息:',data['users'])

    for user in data['users']:
        if user['leftdays'] > 0:
            user['leftdays'] -= 1
    print('修改之后的信息:',data['users'])

    with open('user_info.json', 'w') as file:
        json.dump(data, file, indent=4)


# 设置任务每天零点执行
schedule.every().day.at("00:00").do(task)

def timer_start():
    while True:
        schedule.run_pending()
        time.sleep(60)  # 检查任务是否需要执行的频率


if __name__ == '__main__':
    now = datetime.now()

    # 格式化当前时间为更友好的格式
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

    # 打印格式化后的时间
    print("当前时间是:", formatted_time)
    print("定时器已开启。")
    timer_start()