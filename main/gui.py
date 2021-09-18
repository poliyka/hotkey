import threading
import tkinter as tk
from tkinter import StringVar, ttk
from enum import Enum, auto

import listener

import sys
from os.path import dirname, abspath
CURRENT_DIR = dirname(__file__)
path = abspath(CURRENT_DIR + "/../")
sys.path.append(path)



class App_start:
    def __init__(self, frame):
        self.frame = frame
        self.on_move_text = tk.StringVar()
        self.button()
        self.label()
        self.log_area()
        self.grid_place()

        self.log = self.Log(self.log_tk)

    def get_attr(self, attr):
        return getattr(self, attr, None)

    def label(self):
        self.note_tk = tk.Label(
            self.frame,
            text="熱鍵:\nF2執行腳本\nESC:結束",
            font=("標楷體", 12),
            width=20,
            height=5,
            background="pink",
        )
        self.on_move_tk = tk.Label(
            self.frame,
            text="",
            font=("標楷體", 12),
            width=20,
            height=1,
            textvariable=self.on_move_text
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
                              font=('標楷體', 12),
                              width=22,
                              height=4,
                              bg='white',
                              fg='black',
                              highlightcolor="pink",
                              selectbackground="MidnightBlue",
                              borderwidth=2,
                              )

    def btn_Start_click(self):
        from script import Script
        t = threading.Thread(target=listener.start, args=(self.get_attr, Script))
        t.setName("bin_start")
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

    def grid_place(self):
        self.note_tk.grid(row=0, column=1, pady=2)
        self.on_move_tk.grid(row=1, column=1, pady=2)
        self.log_tk.grid(row=2, column=1, pady=2)
        self.btn_start.grid(row=3, column=1, pady=2)


def closeWindow():
    import os

    win.destroy()
    os._exit(0)


if __name__ == "__main__":
    win = tk.Tk()
    win.geometry("210x250+100+100")
    win.title("鍵鼠自動腳本程式")
    win.attributes("-topmost", 1)
    frame = tk.Frame(win)
    frame.pack()

    App_start(frame)
    win.protocol("WM_DELETE_WINDOW", closeWindow)
    win.mainloop()
