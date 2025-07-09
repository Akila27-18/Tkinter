# task18_button_random_move.py
import tkinter as tk
import random

def move_button(event):
    x = random.randint(0, root.winfo_width() - 100)
    y = random.randint(0, root.winfo_height() - 30)
    btn.place(x=x, y=y)

root = tk.Tk()
root.geometry("400x300")
btn = tk.Button(root, text="Catch Me")
btn.place(x=150, y=100)
btn.bind("<Button-1>", move_button)
root.mainloop()
