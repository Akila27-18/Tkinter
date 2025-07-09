# task19_right_click_popup.py
import tkinter as tk
from tkinter import messagebox

def show_popup(event):
    messagebox.showinfo("Right Click", "You right-clicked!")

root = tk.Tk()
btn = tk.Button(root, text="Right Click Me")
btn.bind("<Button-3>", show_popup)
btn.pack(pady=20)
root.mainloop()
