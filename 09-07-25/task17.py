# task17_label_hover_color.py
import tkinter as tk

def on_enter(e): label.config(bg="lightblue")
def on_leave(e): label.config(bg="SystemButtonFace")

root = tk.Tk()
label = tk.Label(root, text="Hover Over Me", width=20)
label.bind("<Enter>", on_enter)
label.bind("<Leave>", on_leave)
label.pack(pady=20)
root.mainloop()
