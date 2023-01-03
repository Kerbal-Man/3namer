import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=700, bg="#404040")
canvas.pack()

nameChecker = tk.Button(root, text="Run Name Checker")

root.mainloop()
