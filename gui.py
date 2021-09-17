import tkinter as tk
from tkinter import StringVar, ttk
import touch
import threading
import csv


class App_start:
    def __init__(self, frame):
        self.frame = frame

        self.button()
        self.label()
        self.pack_place()

    def label(self):
        self.lb = tk.Label(
            self.frame,
            text="熱鍵:\nF2執行腳本\nESC:結束",
            font=("標楷體", 12),
            width=15,
            height=5,
            bg="Pink",
        )

    def button(self):
        self.btn_start = ttk.Button(
            self.frame,
            text="Start",
            width=10,
            cursor="hand2",
            command=self.btn_Start_click,
        )

    def btn_Start_click(self):
        t = threading.Thread(target=touch.call_start, args=(self.btn_start,))
        t.start()
        self.btn_start.config(state="disable")

    def pack_place(self):
        self.lb.pack()
        self.btn_start.pack()


def closeWindow():
    import os

    win.destroy()
    os._exit(0)


if __name__ == "__main__":
    win = tk.Tk()
    win.geometry("200x130+100+100")
    win.title("古劍自動釣魚程式")
    win.attributes("-topmost", 1)
    frame = tk.Frame(win)
    frame.pack()

    App_start(frame)
    win.protocol("WM_DELETE_WINDOW", closeWindow)
    win.mainloop()
