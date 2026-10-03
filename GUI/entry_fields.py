from tkinter import *
win = Tk()
win.geometry("400x200")
# Using Entry fields for single-line inputs (like obscured passwords with the 'show' flag)
entry_pass = Entry(win, show="*", font=("Arial", 20), bd=5, justify=CENTER)
entry_pass.place(x=50, y=50, width=300, height=50)
win.mainloop()