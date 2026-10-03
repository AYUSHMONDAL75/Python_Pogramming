from tkinter import *
win = Tk()
win.geometry("500x400")
# Using Text boxes for multi-line multi-paragraph text blocks
# Height defines total line rows capacity visible inside the viewframe
text_area = Text(win, font=("Times New Roman", 14), height=8, width=40)
text_area.place(x=10, y=10, width=480, height=300)
win.mainloop()