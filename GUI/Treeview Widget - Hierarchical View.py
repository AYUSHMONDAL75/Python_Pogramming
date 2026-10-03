from tkinter import *
from tkinter import ttk
win = Tk()
win.title("Hierarchical Treeview Showcase")
win.geometry("400x300")
# Initializing the central Treeview component
tree = ttk.Treeview(win)
tree.pack(fill=BOTH, expand=True, padx=10, pady=10)
# Inserting top-level parent categories
node_admin = tree.insert("", END, text="Administration")
node_logistics = tree.insert("", END, text="Logistics")
# Nesting secondary child variables underneath specific parent nodes
tree.insert(node_admin, END, text="John Doe")
tree.insert(node_admin, END, text="Jane Smith")
tree.insert(node_logistics, END, text="Global Shipping")
win.mainloop()