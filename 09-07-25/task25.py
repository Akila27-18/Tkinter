# task25_entry_border_hover.py
import tkinter as tk

def on_enter(e): entry.config(highlightbackground="blue", highlightthickness=2)
def on_leave(e): entry.config(highlightthickness=0)

root = tk.Tk()
entry = tk.Entry(root, highlightthickness=0)
entry.pack(pady=20)
entry.bind("<Enter>", on_enter)
entry.bind("<Leave>", on_leave)
root.mainloop()
