from tkinter import *
# Creating functional python functions to pass to commands
def change_text():
    label_status.config(text="Python", fg="red")
win = Tk()
win.geometry("300x200")
label_status = Label(win, text="Hello", font=("Arial", 30))
label_status.place(x=30, y=30)
# Creating functional buttons, binding user actions using the command attribute
# dynamically changing elements upon clicks
btn_trigger = Button(win, text="OK", command=change_text, font=("Arial", 14))
btn_trigger.place(x=30, y=100, width=100, height=50)
win.mainloop()