from tkinter import *
from tkinter import ttk
win = Tk()
win.geometry("600x400")
# Creating organizational structural framework layouts (Frame) with 3D sunken boundaries
frame_left = Frame(win, width=250, height=350, relief=SUNKEN, bd=4, bg="red")
frame_left.place(x=10, y=10)
# Creating labeled frame containers (LabelFrame) positioning custom text parameters
labelframe_right = LabelFrame(win, text="Python", width=300, height=350, font=("Arial", 12))
labelframe_right.place(x=280, y=10)
win.mainloop()