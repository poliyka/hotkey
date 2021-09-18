import threading
import sys
from collections import deque
from os.path import dirname, abspath

from pynput import keyboard, mouse

CURRENT_DIR = dirname(__file__)
path = abspath(CURRENT_DIR + "/../")
sys.path.append(path)
from script import Script

from get_color import get_color_hex, get_color_rgb
from StringPool import VK_CODE, VK_SHIFT_CODE
from window_capture import capture


class StartListener:
    def __init__(self, get_attr):
        self.get_attr = get_attr
        self.log = self.get_attr("log")
        self.log_deque = deque(maxlen=3)
        self.btn_start = self.get_attr("btn_start")
        self.on_move_text = self.get_attr("on_move_text")
        self.key = None
        self.switch = False
        self.start_listen()
        self.cache_click = tuple()
        self.pk = {
            "get_color_hex": get_color_hex,
            "get_color_rgb": get_color_rgb,
            "VK_CODE": VK_CODE,
            "VK_SHIFT_CODE": VK_SHIFT_CODE,
            "capture": capture,
        }
        self.script = Script(self.pk)

    # 初始監聽
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
        # print(f"Keyboard press: {key}")
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
        pass
        # print(f"Keyboard release: {key}")

    # 滑鼠監聽
    def on_move(self, x, y):
        self.on_move_text.set(f"滑鼠位置: {x}, {y}")
        # print('Pointer moved to {0}'.format((x, y)))
        if self.key == keyboard.Key.esc:
            return False

    def on_click(self, x, y, button, pressed):
        # print("{!= at {1}".format("Pressed" if pressed else "Released", (x, y)))
        if (x, y) != self.cache_click:
            try:
                color = get_color_hex(x, y)
            except:
                color = "None"

            self.log_deque.append((x, y, color))
            self.cache_click = (x, y)

        text = ""
        for i, log in enumerate(self.log_deque):
            text += f"{i+1}. {log[0]}, {log[1]} {log[2]}\n"

        self.log.replace_all(text)

    def on_scroll(self, x, y, dx, dy):
        pass
        # print("Scrolled {0} at {1}".format("down" if dy < 0 else "up", (x, y)))


# 監聽啟動
def start(get_attr):
    StartListener(get_attr)
