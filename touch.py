from StringPool import VK_CODE, VK_SHIFT_CODE

import time
import threading
from pynput import keyboard, mouse
from get_color import get_color_hex
from script import Script


key_ctr = keyboard.Controller()
mouse_ctr = mouse.Controller()

class StartListener:
    def __init__(self, btn_start):
        self.btn_start = btn_start
        self.key = None
        self.switch = False
        self.start_listen()
        self.script = Script()

    # 初始設定
    def start_listen(self):
        threading.Thread(target=self.mouse_listener).start()
        threading.Thread(target=self.keyboard_listener).start()

    def mouse_listener(self):
        with mouse.Listener(
            on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll
        ) as listener:
            listener.join()

    def keyboard_listener(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    # 按鍵監聽
    def on_press(self, key):

        print(f"Keyboard press: {key}")
        self.key = key

        # 結束監聽
        if key == keyboard.Key.esc:
            self.btn_start.config(state="active")
            return False

        # 執行腳本
        if key == keyboard.Key.f2:
            self.switch = False if self.switch else True
            threading.Thread(target=self.keyboard_listener).start()
            if self.script.auto_loop:
                self.on_press("loop")
            else:
                for i in range(self.script.n_loop):
                    self.script.start_script()
                    print(f"{i+1}/{self.script.n_loop}")

            return False
        elif key == "loop":
            if self.switch:
                self.script.start_script()
                self.on_press("loop")


    def on_release(self, key):
        print(f"Keyboard release: {key}")

    # 滑鼠監聽
    def on_move(self, x, y):
        # print('Pointer moved to {0}'.format((x, y)))
        if self.key == keyboard.Key.esc:
            return False

    def on_click(self, x, y, button, pressed):
        print("{0} at {1}".format("Pressed" if pressed else "Released", (x, y)))

    def on_scroll(self, x, y, dx, dy):
        print("Scrolled {0} at {1}".format("down" if dy < 0 else "up", (x, y)))


# 監聽啟動
def call_start(btn_start):
    StartListener(btn_start)
