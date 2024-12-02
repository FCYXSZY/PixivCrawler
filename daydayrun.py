import datetime
import threading
import os
import time

marktime = " 23:12:20"


def func():
    #运行那个turorial.py文件
    os.system("python tutorial.py")
    print("haha")
    # 定为一天
    timer = threading.Timer(86400, func)
    timer.daemon = True  # 设置守护线程模式
    timer.start()


def preFun():
    now_time = datetime.datetime.now()
    marktimes = datetime.datetime.strptime(str(now_time.date()) + marktime, "%Y-%m-%d %H:%M:%S")
    if now_time <= marktimes:
        next_time = marktimes
        print("今日" + marktime + '执行代码')
    else:
        next_time = now_time + datetime.timedelta(days=+1)
        print("明日" + marktime + '执行代码')

    next_year = next_time.date().year
    next_month = next_time.date().month
    next_day = next_time.date().day

    next_time = datetime.datetime.strptime(
        f"{next_year}-{next_month}-{next_day}{marktime}", "%Y-%m-%d %H:%M:%S")
    timer_start_time = (next_time - now_time).total_seconds()
    return timer_start_time


def main():
    timer_start_time = preFun()
    timer = threading.Timer(timer_start_time, func)
    timer.daemon = True  # 设置守护线程
    timer.start()
    print('冷启动后启动 func 的时间:', timer_start_time)

    # 阻止主线程退出，但降低 CPU 消耗
    try:
        while True:
            time.sleep(1)  # 每隔 1 秒休眠一次，几乎不占用 CPU
    except KeyboardInterrupt:
        print("程序被手动终止")


if __name__ == '__main__':
    main()
