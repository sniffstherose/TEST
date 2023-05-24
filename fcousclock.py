import time

def focus_timer(duration):
    start_time = time.time()
    end_time = start_time + duration * 60  # 将分钟转换为秒

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        timer_display = f"{minutes:02d}:{seconds:02d}"
        print(f"Remaining time: {timer_display}", end="\r")
        time.sleep(1)

    print("Time's up! Stay focused!")

# 设置专注时长为25分钟
focus_timer(25)
