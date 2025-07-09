# task21_label_double_click.py
import tkinter as tk

def on_double_click(event):
    label.config(text="You double-clicked me!")

root = tk.Tk()
label = tk.Label(root, text="Double-Click Me", width=25)
label.pack(pady=20)
label.bind("<Double-Button-1>", on_double_click)
root.mainloop()
