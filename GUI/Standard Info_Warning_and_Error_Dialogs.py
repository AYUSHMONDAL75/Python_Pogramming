from tkinter import *
from tkinter import messagebox
def launch_dialogs():
    # 1. Generic information notification message dispatch
    messagebox.showinfo("Python Info", "Operation executed successfully.")
    # 2. Structural caution indicator pop-up dispatch 
    messagebox.showwarning("System Warning", "Unusual threshold detected.")
    # 3. Direct fatal failure diagnostic catch warning dispatch
    messagebox.showerror("Execution Error", "Invalid mathematical expression.")
win = Tk()
win.geometry("200x100")
btn_trigger = Button(win, text="Show Messages", command=launch_dialogs)
btn_trigger.pack(expand=True)
win.mainloop()