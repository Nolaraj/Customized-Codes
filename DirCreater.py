import os
import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()


    file_path = filedialog.askdirectory()

    return file_path

Level0 = ["Scaled Records"]
Level1 = ["Square", "L1", "L2", "L3", "L4", "Rectangle"]
Level2 = ["Gorkha", "Northridge", "SanFernando"]
Level3 = ["Soft", "Medium", "Hard"]

currpath = os.path.join(open_file_dialog(), "Main Folder")
filePaths = []
for h in Level0:
    for i in Level1:
        for j in Level2:
            for k in Level3:
                path = os.path.join(currpath, h , i, j, k)
                if os.path.exists(path) is False:
                    os.makedirs(path)
                filePaths.append(filePaths)


with open("FilePaths.txt", "w") as f:
    for fp in filePaths:
        f.write(str(fp))
        f.write("\n")

