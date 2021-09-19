class Script:
    def __init__(self, pk):
        self.auto_loop = True
        self.n_loop = 2
        self.time = pk.get("time")
        self.keyboard = pk.get("keyboard")
        self.mouse = pk.get("mouse")
        self.key_ctr = self.keyboard.Controller()
        self.mouse_ctr = self.mouse.Controller()
        self.get_color_hex = pk.get("get_color_hex")
        self.get_color_rgb = pk.get("get_color_rgb")
        self.VK_CODE = pk.get("VK_CODE")
        self.VK_SHIFT_CODE = pk.get("VK_SHIFT_CODE")
        self.capture = pk.get("capture")

    def start_script(self):
        self.mouse_ctr.position = (379, 12)
        self.time.sleep(0.5)
        # self.mouse_ctr.click(self.mouse.Button.left)
        # self.time.sleep(0.5)

        self.mouse_ctr.position = (408, 524)
        self.time.sleep(0.5)
        # self.mouse_ctr.click(self.mouse.Button.left)
        # self.time.sleep(0.5)

        self.mouse_ctr.position = (1137, 377)
        self.time.sleep(0.5)
        # self.mouse_ctr.click(self.mouse.Button.left)
        # self.time.sleep(0.5)

        # self.mouse_ctr.position = (379, 12)
        # self.capture(759, 197, 1882, 881)


#############################################
# 範例
#############################################
"""
休息時間設定(秒)
time.sleep(0.05)
將滑鼠定位到x,y
mouse_ctr.position = (680, 337)
移動滑鼠x,y
mouse_ctr.move(680, 337)

滑鼠左鍵單擊。
mouse_ctr.click(mouse.Button.left)
滑鼠左鍵雙擊。
mouse_ctr.click(mouse.Button.left, 2)
滑鼠右鍵單擊。
mouse_ctr.click(mouse.Button.right)
滑鼠中鍵單擊。
mouse_ctr.click(mouse.Button.middle)

模擬拖曳
mouse_ctr.press(mouse.Button.left)
按下左鍵。
mouse_ctr.move(50, 0)
右移50單位。
mouse_ctr.move(0, 50)
下移50單位。
mouse_ctr.release(mouse.Button.left)
釋放左鍵。

按鍵觸發
key_ctr.press(keyboard.Key.shift)
通過按鍵對象 按下shift鍵。

通過長度為1的字元 按下s鍵。
key_ctr.press("s")

掃尾，釋放剛才按下的鍵。
key_ctr.release(keyboard.Key.ctrl)
key_ctr.release(keyboard.Key.shift)
key_ctr.release("s")

自動釋放
with key_ctr.pressed(keyboard.Key.ctrl, keyboard.Key.shift, "s"):
    pass

輸日一串文字
key_ctr.type('Hello world!')
"""
