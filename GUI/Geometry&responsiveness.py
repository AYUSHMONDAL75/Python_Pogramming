from tkinter import *
win = Tk()
win.title("Geometry Configuration")
# Fixing absolute window sizes using the geometry() function (width x height)
win.geometry("600x700")
# Controlling resizing using resizable(False, False) to lock dimensions
win.resizable(False, False)
win.mainloop()