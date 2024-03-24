import tkinter as tk
import os
import sys

from preprocess import clean_text

from tkinter.filedialog import askopenfilename
tk.Tk().withdraw() # part of the import if you are not using other tkinter functions

fn = askopenfilename()
#print("user chose", fn)

if os.path.splitext(fn)[1] == ".txt":
    # Open the file in read mode
    with open(fn, "r", encoding='utf-8') as file:
        # Read the contents of the file
        text = file.read()

#THIS WORKS.

#MAYBE WHAT WE DO IS HAVE A PYTHON CODE IN RENPY THAT BASICALLY CALLS A SUBPROCESS THAT MAKE'S USE OF MCQ_UTILS SO WE CAN OUTPUT THAT TO THE USER, EACH PART.

#preprocessing

text = clean_text(text)
#print(repr(text))

filename = sys.argv[1]

base_path = os.getcwd()
relative_path = f"kodigo\\game\\python\\docs\\{filename}.txt"
fp = os.path.join(base_path, relative_path)

with open(fp, "w") as file:
    file.write(text)