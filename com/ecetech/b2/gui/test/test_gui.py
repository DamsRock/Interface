import tkinter as tk
from tkinter import ttk as tktw


class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("640x480")
        self.minsize(width=640, height=480)
        self.fm = FrameMain(self, background="pink")
        self.fb = FrameBottom(self, background="lightblue")
        self.fl = FrameLeft(self.fm, background="yellow")
        self.fr = FrameRight(self.fm, background="green")
        self.fa = FrameAction(self.fr, background="orange")
        self.fc = FrameChat(self.fr, background="blue")
        self.tm = TopMenu(self)
        self.config(menu=self.tm)
        # self.ab = ActionBar(self.fa, width=0, height=0)
        # self.ai = ActionInfo(self.ab, width=0, height=0)
        # self.ab.add(self.ai, text="Info", state="normal")
        self.c = CanvasArea(self.fl, width=0, height=0)


class FrameMain(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(fill=tk.BOTH, expand=1)


class FrameLeft(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(fill=tk.BOTH, expand=1, side="left")


class CanvasArea(tk.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(fill=tk.BOTH, expand=1)


class FrameRight(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(fill=tk.BOTH, expand=1, side="right")


class FrameChat(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(fill=tk.BOTH, expand=1, side="bottom")


class FrameAction(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(fill=tk.BOTH, expand=1, side="top")


class ActionBar(tktw.Notebook):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(expand=1, fill=tk.BOTH)


class ActionInfo(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(fill=tk.BOTH, expand=1)


class FrameBottom(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(fill=tk.BOTH)
        self.cb = ComboboxCommands(self, width=10, state="readonly")
        self.cl = CommandLine(self, relief="ridge", bd=2)
        self.bs = ButtonSend(self, text="Send", relief="ridge")


class ComboboxCommands(tktw.Combobox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(side="left", fill=tk.BOTH)


class CommandLine(tk.Entry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(side="left", fill=tk.BOTH, expand=1)


class ButtonSend(tk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(side="right")


class TopMenu(tk.Menu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_cascade(label="Menu")


if __name__ == "__main__":
    w = Window()

    imgsrc = tk.PhotoImage(file="lion....gif")
    img = w.c.create_image(0, 0, anchor="nw", image=imgsrc)

    w.mainloop()
