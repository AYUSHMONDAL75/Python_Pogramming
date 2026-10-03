from tkinter import *
from tkinter import filedialog
def execute_read_pipeline():
    # Strict extension constraint mapping definitions array
    extension_filters = (("Text Documents", "*.txt"), ("All Files", "*.*"))
    # Prompts target selector directly, yielding the strict absolute path
    selected_path = filedialog.askopenfilename(title="Open Text File", 
filetypes=extension_filters)
    if selected_path:
        print(f"Target file system access point established at: {selected_path}")
        # Initialize an explicit read operations context stream targeting local text blocks
        with open(selected_path, "r") as local_stream:
            contents = local_stream.read()
            print("--- File Contents Gathered ---")
            print(contents)
win = Tk()
win.geometry("200x100")
Button(win, text="Select & Read File", command=execute_read_pipeline).pack(expand=True)
win.mainloop()