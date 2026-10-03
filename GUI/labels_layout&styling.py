from tkinter import *
win = Tk()
win.geometry("500x200")
win.config(bg="yellow")
# Labels: Displaying static texts, adjusting font family/sizes, text styles (bold/italic)
# text alignments, background matching, and applying 3D relief effects (sunken)
label_title = Label(
    win, 
    text="Hello Python", 
    font=("Times New Roman", 50, "bold", "italic"),
    bg="yellow",
    fg="black",
    relief=SUNKEN,
    bd=5,
    anchor=W # Anchoring text to the West side
)
label_title.place(x=100, y=100, width=340, height=70)
win.mainloop()