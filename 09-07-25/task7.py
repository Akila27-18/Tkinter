# task7_label_hover_color.py
import tkinter as tk

def on_enter(e): lbl.config(fg="red")
def on_leave(e): lbl.config(fg="black")

root = tk.Tk()
lbl = tk.Label(root, text="Hover over me", fg="black")
lbl.bind("<Enter>", on_enter)
lbl.bind("<Leave>", on_leave)
lbl.pack()
root.mainloop()
