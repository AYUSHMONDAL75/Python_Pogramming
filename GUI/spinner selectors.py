from tkinter import *
from tkinter import ttk
win = Tk()
win.geometry("300x200")
# Integrating numeric spinner selectors (Spinbox) from the advanced ttk subset
# Sets constraints securely using clear from_ and to boundary flags
spin_range = ttk.Spinbox(win, from_=0, to=10, wrap=False, font=("Arial", 16))
spin_range.place(x=50, y=50, width=100, height=30)
win.mainloop()