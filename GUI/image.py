from tkinter import *
win = Tk()
win.geometry("400x400")
# Loading images using the PhotoImage function
file_image = PhotoImage(file="phone_icon.png")
# Anchoring them onto labels alone
label_graphic = Label(win, image=file_image)
label_graphic.pack()
win.mainloop()