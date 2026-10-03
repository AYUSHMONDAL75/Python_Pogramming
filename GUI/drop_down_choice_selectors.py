from tkinter import *
# Importing the advanced ttk module wrapper class explicitly
from tkinter import ttk 
win = Tk()
win.geometry("400x200")
languages_list = ["C#", "C++", "Python", "Java"]
# Integrating drop-down choice selectors (ComboBox) from ttk class
combo_menu = ttk.Combobox(win, values=languages_list, font=("Arial", 18))
combo_menu.place(x=50, y=50, width=300, height=40)
combo_menu.set("WSCube Tech") # Setting initial prompt text values
win.mainloop()