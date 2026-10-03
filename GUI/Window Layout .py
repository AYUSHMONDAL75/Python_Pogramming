from tkinter import *
from tkinter import ttk
win = Tk()
win.geometry("600x400")
# Integrating structural organizational framing tab controls (Notebook)
notebook_control = ttk.Notebook(win)
notebook_control.pack(fill=BOTH, expand=True, pady=10)
# Building individual framework layout sheets to anchor inside the tab system
tab_new = ttk.Frame(notebook_control, width=500, height=350)
tab_open = ttk.Frame(notebook_control, width=500, height=350)
tab_new.pack(fill=BOTH, expand=True)
tab_open.pack(fill=BOTH, expand=True)
# Registering baseline menu titles directly to target navigation elements
notebook_control.add(tab_new, text="New")
notebook_control.add(tab_open, text="Open")
win.mainloop()