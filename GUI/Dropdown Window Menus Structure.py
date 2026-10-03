from tkinter import *
def sample_command():
    print("Menu Command Clicked")
win = Tk()
win.geometry("400x300")
# Building full dropdown file navigation setups utilizing main menu bars
main_menu = Menu(win)
win.config(menu=main_menu)
# Configuring a file dropdown container, dropping explicit dash separation dividers via tearoff
file_dropdown = Menu(main_menu, tearoff=0)
# Registering nested commands smoothly into targeted tracking layers
file_dropdown.add_command(label="New File", command=sample_command)
file_dropdown.add_command(label="Open Folder")
# Building structural layout segmentation lines across actions using add_separator()
file_dropdown.add_separator()
file_dropdown.add_command(label="Save File")
# Registering standard root cascade links securely to parent window blocks
main_menu.add_cascade(label="File", menu=file_dropdown)
main_menu.add_cascade(label="Edit")
win.mainloop()