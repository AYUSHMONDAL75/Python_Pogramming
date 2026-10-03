from tkinter import *
from tkinter import colorchooser
def trigger_color_picker():
    # Opens native selection palette directly to user space
    # Returns an evaluation tuple tracking precise RGB mixes alongside individual Hex keys
    color_profile = colorchooser.askcolor(title="Pick App Background Color")
    print(f"Full Color data profile object parsed: {color_profile}")
    # Verify a valid selection was returned before applying background configuration updates
    if color_profile[1]:
        win.config(bg=color_profile[1])
win = Tk()
win.geometry("300x200")
btn_color = Button(win, text="Modify Window Color", command=trigger_color_picker)
btn_color.pack(expand=True)
win.mainloop()