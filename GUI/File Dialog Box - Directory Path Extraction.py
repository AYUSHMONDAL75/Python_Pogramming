from tkinter import *
from tkinter import filedialog
def capture_directory_path():
    # Captures target folder root mappings directly 
    isolated_folder_path = filedialog.askdirectory(title="Select Destination Folder Target")
    if isolated_folder_path:
        print(f"Destination folder tracking directory path extracted: {isolated_folder_path}")
win = Tk()
win.geometry("200x100")
Button(win, text="Locate Folder Root", command=capture_directory_path).pack(expand=True)
win.mainloop()