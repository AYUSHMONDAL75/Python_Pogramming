from tkinter import *
from tkinter.messagebox import showinfo
import random
win = Tk()
win.title("Love App")
width = 900
height = 700
sys_width = win.winfo_screenwidth()
sys_height = win.winfo_screenheight()
c_x = int(sys_width/2 - width/2)
c_y = int(sys_height/2 - height/2)
win.geometry(f"{width}x{height}+{c_x}+{c_y}")
win.resizable(False, False)
win.config(bg="black")
win.title("Proposal")

# Label
label = Label(win, text="I Like You, Do You Like Me.....?", font=("Bell MT", 30, "bold"), bg="black", fg="blue")
label.place(x = 170, y = 30)

# Yes button function
def yes_clicked():
    showinfo(title="My Love ❤️", message="I know you like me 😊")

# Yes Button
yes = Button(win, text="YES", font=("Bell MT", 20, "bold"), bg="black", fg="yellow", cursor="hand2", command=yes_clicked, relief="solid",activebackground="green")
yes.place(x= 350, y = 100)

# Function to move NO button
def move_button(event):
    x = random.randint(50, 800)
    y = random.randint(120, 600)
    no.place(x=x, y=y)

# NO Button
no = Button(win, text="NO", font=("Bell MT", 20, "bold"), bg="black", fg="yellow", cursor="hand2",relief="solid", activebackground="yellow")
no.place(x=450, y=100)

# Move button when mouse enters it
no.bind("<Enter>", move_button)

#Function to Exit Button
def exit():
    win.destroy()
    return

#Exit button
exit = Button(win, text="EXIT", font=("Bahnschrift Light", 15, "bold"), bg="black", fg="red", cursor="hand2",relief="solid", activebackground="yellow",command=exit)
exit.place(x=790, y=650)
win.mainloop()