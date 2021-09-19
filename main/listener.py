import threading
import time
import pickle
import os
from collections import deque

from pynput import keyboard, mouse

from get_color import get_color_hex, get_color_rgb
from vk_pool import VK_CODE, VK_SHIFT_CODE
from window_capture import capture


class StartListener:
    def __init__(self, get_attr, script, mode):
        self.mode = mode
        self.get_attr = get_attr
        self.log = self.get_attr("log")
        self.btn_start = self.get_attr("btn_start")
        self.on_move_text = self.get_attr("on_move_text")
        self.script_mode_text = self.get_attr("script_mode_text")
        self.pickle_path = "mouse_record.pickle"
        self.n_loop = 1
        self.key = None
        self.switch = False
        self.cache_click = tuple()
        self.pk = {
            "time": time,
            "keyboard": keyboard,
            "mouse": mouse,
            "get_color_hex": get_color_hex,
            "get_color_rgb": get_color_rgb,
            "VK_CODE": VK_CODE,
            "VK_SHIFT_CODE": VK_SHIFT_CODE,
            "capture": capture,
        }
        self.script = script.Script(self.pk)
        self.mouse_listener = mouse.Listener(
            on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll
        )

        if self.mode == "default":
            self.log_deque = deque(maxlen=3)
            self._default_mode()
        elif self.mode == "mouse_record":
            self.log_deque = deque()
            self._mouse_record_mode()

    def mouse_listener_start(self):
        self.mouse_listener.start()

    def keyboard_listener_start(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    # 按鍵監聽
    def on_press(self, key):
        # print(f"Keyboard press: {key}")
        self.key = key

        # 結束監聽
        if key == keyboard.Key.esc:
            return self._esc(key)
        # 執行腳本
        if key == keyboard.Key.f2:
            return self._f2(key)
        # loop腳本
        if key == "loop":
            return self._loop(key)
        # n_loop腳本
        if key == "n_loop":
            return self._n_loop(key)

    def on_release(self, key):
        pass
        # print(f"Keyboard release: {key}")

    # 滑鼠監聽
    def on_move(self, x, y):
        self.on_move_text.set(f"滑鼠位置: {x}, {y}")
        # print('Pointer moved to {0}'.format((x, y)))

    def on_click(self, x, y, button, pressed):
        # print("{!= at {1}".format("Pressed" if pressed else "Released", (x, y)))

        if self.mode == "default":
            self._log_msg_on_click(x, y, button, pressed)
        elif self.mode == "mouse_record":
            self._log_msg_on_click(x, y, button, pressed)
            self._mouse_record(x, y, button, pressed)

    def on_scroll(self, x, y, dx, dy):
        pass
        # print("Scrolled {0} at {1}".format("down" if dy < 0 else "up", (x, y)))

    # Keyboard Event
    def _f2(self, key):
        self.switch = False if self.switch else True
        if self.switch:
            t1 = threading.Thread(target=self.keyboard_listener_start)
            t1.setName("new_keyboard")
            t1.start()
        else:
            self.n_loop = 0
            self.script_mode_text.set(f"腳本模式: Stop")
            return False

        if self.script.auto_loop:
            self.script_mode_text.set(f"腳本模式: Auto")
            self.on_press("loop")
        else:
            self.on_press("n_loop")

    def _f3(self, key):
        self.switch = False if self.switch else True
        if self.switch:
            t1 = threading.Thread(target=self.keyboard_listener_start)
            t1.setName("new_keyboard")
            t1.start()
        else:
            self.n_loop = 0
            self.script_mode_text.set(f"腳本模式: Stop")
            return False

        if self.script.auto_loop:
            self.script_mode_text.set(f"腳本模式: Auto")
            self.on_press("loop")
        else:
            self.on_press("n_loop")

    def _loop(self, key):
        if self.switch:
            self.script.main()
            self.on_press("loop")

    def _n_loop(self, key):
        if self.switch:
            if self.n_loop <= self.script.n_loop:
                self.script_mode_text.set(f"腳本模式: {self.n_loop}/{self.script.n_loop}")
                self.script.main()
                self.n_loop += 1
                self.on_press("n_loop")

    def _esc(self, key):
        self.btn_start.config(state="active")
        self.script_mode_text.set(f"腳本模式: Stop")
        self.switch = False
        self.mouse_listener.stop()
        return False

    # Mouse Event
    def _log_msg_on_click(self, x, y, button, pressed):
        if (x, y) != self.cache_click:
            try:
                color = get_color_hex(x, y)
            except:
                color = "None"

            self.log_deque.appendleft((x, y, color))
            self.cache_click = (x, y)

        text = ""
        q_len = len(self.log_deque)
        for log in self.log_deque:
            text += f"{q_len}. {log[0]}, {log[1]} {log[2]}\n"
            q_len -= 1

        self.log.replace_all(text)

    def _mouse_record(self, x, y, button, pressed):
        df = pickle_load(self.pickle_path)
        print(df)
        pickle_save(self.pickle_path, self.log_deque)



    # Mode
    def _default_mode(self):
        self.script_mode_text.set(f"腳本模式: Stop")
        t1 = threading.Thread(target=self.mouse_listener_start)
        t2 = threading.Thread(target=self.keyboard_listener_start)
        t1.setName("start_mouse")
        t2.setName("start_keyboard")
        t1.start()
        t2.start()

    def _mouse_record_mode(self):
        self.script_mode_text.set(f"滑鼠錄製模式: Start")
        t1 = threading.Thread(target=self.mouse_listener_start)
        t1.setName("start_mouse")
        t1.start()


# 監聽啟動
def start(get_attr, script, mode="default"):
    StartListener(get_attr, script, mode)


def pickle_load(file_name):
    if not os.path.isfile(file_name):
        return False
    with open(file_name, 'rb') as pickle_file:
        return pickle.load(pickle_file)

def pickle_save(file_name, data):
    with open(file_name, 'wb') as f:
        pickle.dump(data, f)
