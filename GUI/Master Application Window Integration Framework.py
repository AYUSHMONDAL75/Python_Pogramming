from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# Global event framework and exit callback intercept handler
def execute_graceful_shutdown():
    # Prompt user configuration before terminating core runtime loop
    confirm_exit = messagebox.askyesno("Exit Workspace", "Are you sure you want to close the Tkinter Masterclass workspace?")
    if confirm_exit:
        print("Closing application workspace safely.")
        win.destroy()
# Base window configuration setup
win = Tk()
win.title("Python Tkinter GUI Development Masterclass - Complete Workspace")
win.geometry("800x600")
win.config(bg="#f0f0f0")
# Intercept default OS close ('X') clicks to route through custom confirmation
win.protocol("WM_DELETE_WINDOW", execute_graceful_shutdown)
# 1. Structural Master Header Block Placement
header_frame = Frame(win, bg="#333333", height=60)
header_frame.pack(side=TOP, fill=X)
lbl_title = Label(header_frame, text="Tkinter GUI Masterclass Workspace", font=("Arial", 16, 
"bold"), bg="#333333", fg="white")
lbl_title.pack(pady=15)
# 2. Centered Interactive Sandbox Workspace Area
# This layout acts as the canvas where modular snippets can be positioned
sandbox_canvas = LabelFrame(win, text=" Interactive Component Sandbox Space ", font=("Arial", 
11, "bold"), bd=2, relief=GROOVE)
sandbox_canvas.pack(fill=BOTH, expand=True, padx=20, pady=20)
# Sample placeholder anchoring inside the sandbox region
lbl_welcome = Label(sandbox_canvas, text="Select or write standard module code segments to populate this layout view.", font=("Arial", 12, "italic"))
lbl_welcome.pack(expand=True)
# 3. Base Window Footer Status Label Layout Anchoring 
footer_bar = Label(win, text="Workspace Engine Status: Ready", bd=1, relief=SUNKEN, anchor=W, 
bg="#e0e0e0", font=("Arial", 10))
footer_bar.pack(side=BOTTOM, fill=X)
# Start execution loop pipeline to keep workspace alive
win.mainloop()