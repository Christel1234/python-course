from tkinter.filedialog import askdirectory
from tkinter import Tk
import os
import hashlib

Tk().withdraw()
path = askdirectory(title="Select folder")
dirs = os.walk(path)
newFiles = []

for folder, subfolder, files in dirs:
    for file in files:
        filepath = os.path.join(folder, file)
        hash = hashlib.md5(open(filepath, "rb").read()).hexdigest()
        if hash in newFiles:
            os.remove(filepath)
            print(f"{filepath} has been deleted")
        else:
            newFiles.append(hash)
