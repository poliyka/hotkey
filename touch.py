from StringPool import VK_CODE, VK_SHIFT_CODE

import time
import threading
from pynput import keyboard, mouse
from pynput.keyboard import KeyCode


key_ctr = keyboard.Controller()
mouse_ctr = mouse.Controller()


class StartListener:
    def __init__(self, btn_start):
        self.btn_start = btn_start
        self.key = None
        self.start_listen()

    # 初始設定
    def start_listen(self):
        listen_mouse = threading.Thread(target=self.mouse_listener)
        listen_keyboard = threading.Thread(target=self.keyboard_listener)
        listen_mouse.start()
        listen_keyboard.start()

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

    def on_release(self, key):
        print(f"Keyboard release: {key}")
        # 執行腳本
        if key == keyboard.Key.f2:
            self.work_script()
        keyboard.KeyCode.from_vk()
        # 結束按鈕
        if key == keyboard.Key.esc:
            self.key = key
            self.btn_start.config(state="active")
            return False

    # 滑鼠監聽
    def on_move(self, x, y):
        # print('Pointer moved to {0}'.format((x, y)))
        if self.key == keyboard.Key.esc:
            return False

    def on_click(self, x, y, button, pressed):
        print(button)
        print("{0} at {1}".format("Pressed" if pressed else "Released", (x, y)))

    def on_scroll(self, x, y, dx, dy):
        print("Scrolled {0} at {1}".format("down" if dy < 0 else "up", (x, y)))

    # 撰寫腳本位置
    def work_script(self):
        # 休息時間設定(秒)
        # time.sleep(0.05)
        # 將滑鼠定位到x,y
        # mouse_ctr.position = (680, 337)
        # 移動滑鼠x,y
        # mouse_ctr.move(680, 337)

        # 滑鼠左鍵單擊。
        # mouse_ctr.click(mouse.Button.left)
        # 滑鼠左鍵雙擊。
        # mouse_ctr.click(mouse.Button.left, 2)
        # 滑鼠右鍵單擊。
        # mouse_ctr.click(mouse.Button.right)
        # 滑鼠中鍵單擊。
        # mouse_ctr.click(mouse.Button.middle)

        # 模擬拖曳
        # mouse_ctr.press(mouse.Button.left)
        # 按下左鍵。
        # mouse_ctr.move(50, 0)
        # 右移50單位。
        # mouse_ctr.move(0, 50)
        # 下移50單位。
        # mouse_ctr.release(mouse.Button.left)
        # 釋放左鍵。

        # 按鍵觸發
        key_ctr.press(keyboard.Key.shift)
        # 通過按鍵對象 按下shift鍵。

        # key_ctr.press("s")
        # 通過長度為1的字元 按下s鍵。

        # 掃尾，釋放剛才按下的鍵。後面我會說更簡單、優雅的辦法。
        # key_ctr.release(keyboard.Key.ctrl)
        # key_ctr.release(keyboard.Key.shift)
        # key_ctr.release("s")

        # with key_ctr.pressed(keyboard.Key.ctrl, keyboard.Key.shift, "s"):
        #     pass
        # key_ctr.type('Hello world!')


# 監聽啟動
def call_start(btn_start):
    StartListener(btn_start)
