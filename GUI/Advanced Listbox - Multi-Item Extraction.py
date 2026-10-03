from tkinter import *
def capture_selections():
    # Extracts an array tuple representing the active selected element indices
    selected_indices = list_box.curselection()
    # Resolves corresponding string values mapped across selected indices
    selected_values = [list_box.get(i) for i in selected_indices]
    print(f"Active Multi-Selection Profile: {selected_values}")
win = Tk()
win.title("Multi-Select Processing List")
win.geometry("400x350")
# Configuring the workspace list element into an EXTENDED selection matrix mode
list_box = Listbox(win, font=("Arial", 14), selectmode=EXTENDED)
list_box.place(x=50, y=20, width=300, height=180)
items = ["Data Science", "Machine Learning", "Artificial Intelligence", "Deep Learning"]
for item in items:
    list_box.insert(END, item)
# Trigger button executing data index reads across selection streams
btn_read = Button(win, text="Print Selected Items", font=("Arial", 12), 
command=capture_selections)
btn_read.place(x=100, y=230, width=200, height=40)
win.mainloop()