from tkinter import *
win = Tk()
win.geometry("300x200")
# Utilizing an IntVar tracking variable to cleanly group radial elements
radio_var = IntVar()
# Deploying single-option radial selectors (Radiobutton) using global tracking variables
rb_opt1 = Radiobutton(win, text="Python", variable=radio_var, value=1, font=("Arial", 16))
rb_opt2 = Radiobutton(win, text="Java", variable=radio_var, value=2, font=("Arial", 16))
rb_opt1.pack(anchor=W)
rb_opt2.pack(anchor=W)
win.mainloop()