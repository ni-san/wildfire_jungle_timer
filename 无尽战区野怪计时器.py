import tkinter as tk
import keyboard  # 使用 keyboard 库来监听全局快捷键
from tkinter import font

# 定义一个列表来保存所有的倒计时窗口
countdown_windows = []

# 创建 Tk 实例和自定义字体
root = tk.Tk()
root.withdraw()

custom_font = font.Font(family="Helvetica", size=8)


def keep_on_top(window):
    window.attributes("-topmost", True)
    window.after(1000, keep_on_top, window)


def countdown(label, counter, repeat_reset_time):
    counter -= 1
    label.config(text=str(counter))
    if counter >= 0:
        label.after(1000, countdown, label, counter, repeat_reset_time)
    else:
        label.config(text=str(repeat_reset_time))
        countdown(label, repeat_reset_time, repeat_reset_time)


def create_window(position, initial_counter, repeat_time):
    bg_color = "black"
    window = tk.Toplevel()
    window.attributes("-topmost", True)
    window.attributes("-transparentcolor", bg_color)
    window.overrideredirect(True)

    label = tk.Label(window, text=str(initial_counter), font=custom_font, fg="white", bg=bg_color)
    label.pack()

    x, y = position
    window.geometry(f"+{x}+{y}")

    keep_on_top(window)

    countdown(label, initial_counter, repeat_time)

    countdown_windows.append(window)


# 开始流沙计时的函数
def begin_liusha():
    print("流沙黄点开始计时！")
    clear_all()  # 清除所有已有的计时窗口
    # 流沙场景的时间和位置
    initial_times = [80, 80, 110, 140, 170, 170, 200, 200, 290, 290]
    positions = [(2312, 215), (2520, 215), (2358, 250), (2472, 250),
                 (2388, 285), (2440, 285), (2395, 235), (2440, 235),
                 (2323, 300), (2507, 300)]
    repeat_time1 = 120
    repeat_time2 = 180
    # 创建流沙场景的计时窗口
    for i, pos in enumerate(positions):
        if i < 4:
            create_window(pos, initial_times[i], repeat_time1)
        else:
            create_window(pos, initial_times[i], repeat_time2)


# 开始空港计时的函数
def begin_konggang():
    clear_all()  # 清除所有已有的计时窗口
    print("空港黄点开始计时！")
    # 空港场景的时间和位置
    initial_times = [50, 50, 110, 110]
    positions = [(2290, 250), (2480, 250), (2355, 290), (2435, 290)]
    repeat_time = 120
    # 创建空港场景的计时窗口
    for i, pos in enumerate(positions):
        create_window(pos, initial_times[i], repeat_time)


# 清除所有计时窗口的函数
def clear_all():
    for window in countdown_windows:
        window.destroy()
    countdown_windows.clear()
    print("所有计时窗口已清除。")


if __name__ == "__main__":
    print("希望大家游戏愉快，如果遇到一只灰太狼，请爱护他。")
    print("请以管理员模式运行！当人物进入流沙地图时开始计时。")
    print("按下ctrl+shift+j开始流沙计时！")
    print("按下ctrl+shift+k开始空港计时！")
    print("按下ctrl+shift+l清除计时器！")
    print("退出请直接点击程序右上角。")

    # 注册快捷键
    keyboard.add_hotkey('ctrl+shift+j', begin_liusha)
    keyboard.add_hotkey('ctrl+shift+k', begin_konggang)
    keyboard.add_hotkey('ctrl+shift+l', clear_all)

    try:
        root.mainloop()  # 主事件循环
    except KeyboardInterrupt:
        print('程序已经通过按键中断退出。')

# 打包代码   pyinstaller --onefile 无尽战区野怪计时器.py
