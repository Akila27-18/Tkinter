# task46_label_click_color_change.py
import tkinter as tk

def change_color(event):
    label.config(fg="green" if label.cget("fg") == "black" else "black")

root = tk.Tk()
label = tk.Label(root, text="Click me to change color", fg="black", font=("Arial", 14))
label.pack(pady=20)
label.bind("<Button-1>", change_color)
root.mainloop()
