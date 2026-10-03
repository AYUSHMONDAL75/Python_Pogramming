from tkinter import *
from tkinter import ttk
win = Tk()
win.geometry("200x400")
# Integrating functional sliders (Scale) tracking numerical adjustments 
# Configuring orientation to match a vertical alignment flow
slider_scale = ttk.Scale(win, from_=0, to=100, orient=VERTICAL, length=300)
slider_scale.place(x=50, y=20)
win.mainloop()