# task1_self_disable_button.py
import tkinter as tk

def disable_button(btn):
    btn.config(state="disabled")

root = tk.Tk()
btn = tk.Button(root, text="Click to Disable", command=lambda: disable_button(btn))
btn.pack(pady=20)
root.mainloop()
