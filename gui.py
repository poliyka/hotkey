import threading
import tkinter as tk
from tkinter import StringVar, ttk

import listener


class App_start:
    def __init__(self, frame):
        self.frame = frame
        self.log_var = None
        self.button()
        self.label()
        self.log_area()
        self.pack_place()

        self.log = self.Log(self.log_tk)
        self.log.replace_all("Hello world!")

    def label(self):
        self.lb = tk.Label(
            self.frame,
            text="熱鍵:\nF2執行腳本\nESC:結束",
            font=("標楷體", 12),
            width=20,
            height=5,
        )

    def button(self):
        self.btn_start = ttk.Button(
            self.frame,
            text="Start",
            width=20,
            cursor="hand2",
            command=self.btn_Start_click,
        )


    def log_area(self):
        self.log_tk = tk.Text(self.frame,
                              font=('標楷體', 10),
                              width=22,
                              height=4,
                              bg='white',
                              fg='black',
                              highlightcolor="pink",
                              selectbackground="MidnightBlue",
                              borderwidth=2,
                              )

    def btn_Start_click(self):
        t = threading.Thread(target=listener.start, args=(self.btn_start,))
        t.start()
        self.btn_start.config(state="disable")

    class Log:
        def __init__(self, log_tk):
            self.log_tk = log_tk

        def replace_all(self, text):
            self.log_tk.delete(1.0,"end")
            self.log_tk.insert(1.0, text)

        def replace_line(self, text, start, end):
            self.log_tk.delete(start, end)
            self.log_tk.insert(start, text)

    def pack_place(self):
        self.lb.pack()
        self.log_tk.pack()
        self.btn_start.pack()


def closeWindow():
    import os

    win.destroy()
    os._exit(0)


if __name__ == "__main__":
    win = tk.Tk()
    win.geometry("200x200+100+100")
    win.title("古劍自動釣魚程式")
    win.attributes("-topmost", 1)
    frame = tk.Frame(win)
    frame.pack()

    App_start(frame)
    win.protocol("WM_DELETE_WINDOW", closeWindow)
    win.mainloop()
