# task47_hover_resize_label.py
import tkinter as tk

def enlarge(e): label.config(font=("Arial", 20))
def shrink(e): label.config(font=("Arial", 12))

root = tk.Tk()
label = tk.Label(root, text="Hover over me", font=("Arial", 12))
label.pack(pady=20)
label.bind("<Enter>", enlarge)
label.bind("<Leave>", shrink)
root.mainloop()
