import sys
import importlib
import threading

import tkinter as tk
from tkinter import scrolledtext
from os.path import abspath, dirname
from tkinter import ttk

import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(2)
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(2) / 100

CURRENT_DIR = dirname(__file__)
path = abspath(CURRENT_DIR + "/../")
sys.path.append(path)
import listener
import script


class App_start:
    def __init__(self, frame):
        self.frame = frame
        self.on_move_text = tk.StringVar()
        self.script_mode_text = tk.StringVar()
        self.button()
        self.label()
        self.log_area()
        self.spinbox()
        self.grid_layout()

        # after create
        self.log = self.Log(self.log_tk)
        self.mouse_record_spinbox_tk.set(1)

    def get_attr(self, attr):
        return getattr(self, attr, None)

    def label(self):
        self.note_tk = tk.Label(
            self.frame,
            text="熱鍵:\nF2執行腳本\nESC:結束監聽",
            font=("標楷體", 12),
            justify="left",
            width=20,
            height=5,
            background="#add8e6",
        )
        self.on_move_tk = tk.Label(
            self.frame,
            font=("標楷體", 12),
            width=20,
            height=1,
            textvariable=self.on_move_text,
        )
        self.script_mode_tk = tk.Label(
            self.frame,
            font=("標楷體", 12),
            width=20,
            height=1,
            textvariable=self.script_mode_text,
        )

    def button(self):
        self.btn_start_tk = ttk.Button(
            self.frame,
            text="Start",
            width=20,
            cursor="hand2",
            command=self.btn_Start_tk_click,
        )
        self.btn_record_mouse_tk = ttk.Button(
            self.frame,
            text="錄製滑鼠",
            width=20,
            cursor="hand2",
            command=self.btn_record_mouse_tk_click,
        )
        self.btn_record_mouse_tk_start = ttk.Button(
            self.frame,
            text="執行錄製",
            width=20,
            cursor="hand2",
            command=self.btn_record_mouse_tk_start_click,
        )

    def log_area(self):
        self.log_tk = scrolledtext.ScrolledText(
            self.frame,
            width=22,
            height=5,
            wrap="word",
            font=("標楷體", 12),
            bg="#f5f5f5",
            fg="#00008a",
            selectforeground="#ffa500",
            selectbackground="#8b008b",
            borderwidth=2,
        )

    def spinbox(self):
        self.mouse_record_spinbox_tk = ttk.Spinbox(
            self.frame,
            from_=-1,
            to=999999,
            increment=1,
            wrap=True,
        )

    # command function
    def btn_Start_tk_click(self):
        importlib.reload(script)
        t = threading.Thread(target=listener.start, args=(self.get_attr, script))
        t.setName("bin_start")
        t.start()
        self.btn_disable()

    def btn_record_mouse_tk_click(self):
        t = threading.Thread(target=listener.start, args=(self.get_attr, script, "mouse_record"))
        t.setName("mouse_record")
        t.start()
        self.btn_disable()

    def btn_record_mouse_tk_start_click(self):
        t = threading.Thread(
            target=listener.start, args=(self.get_attr, script, "mouse_record_start")
        )
        t.setName("mouse_record_start")
        t.start()
        self.btn_disable()

    def btn_disable(self):
        self.btn_start_tk.config(state="disable")
        self.btn_record_mouse_tk.config(state="disable")
        self.mouse_record_spinbox_tk.config(state="disable")
        self.btn_record_mouse_tk_start.config(state="disable")

    def btn_active(self):
        self.btn_start_tk.config(state="active")
        self.btn_record_mouse_tk.config(state="active")
        self.mouse_record_spinbox_tk.config(state="active")
        self.btn_record_mouse_tk_start.config(state="active")

    class Log:
        def __init__(self, log_tk):
            self.log_tk = log_tk

        def replace_all(self, text):
            self.log_tk.delete(1.0, "end")
            self.log_tk.insert(1.0, text)

        def replace_line(self, text, start, end):
            self.log_tk.delete(start, end)
            self.log_tk.insert(start, text)

    # layout
    def grid_layout(self):
        self.note_tk.grid(row=0, column=1, pady=2)
        self.on_move_tk.grid(row=1, column=1, pady=1)
        self.script_mode_tk.grid(row=2, column=1, pady=1)
        self.log_tk.grid(row=3, column=1, pady=2)
        self.btn_start_tk.grid(row=4, column=1, pady=2)
        self.btn_record_mouse_tk.grid(row=5, column=1, pady=2)
        self.mouse_record_spinbox_tk.grid(row=6, column=1, pady=2)
        self.btn_record_mouse_tk_start.grid(row=7, column=1, pady=2)


def closeWindow():
    import os

    win.destroy()
    os._exit(0)


if __name__ == "__main__":
    win = tk.Tk()
    w = int(210 * ScaleFactor)
    h = int(340 * ScaleFactor)
    dw = int(100 * ScaleFactor)
    dh = int(100 * ScaleFactor)
    geo = f"{w}x{h}+{dw}+{dh}"
    win.geometry(geo)
    win.title("鍵鼠自動腳本程式")
    win.attributes("-topmost", 1)
    frame = tk.Frame(win)
    frame.pack()

    App_start(frame)
    win.protocol("WM_DELETE_WINDOW", closeWindow)
    win.mainloop()
