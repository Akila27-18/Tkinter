# task6_enable_after_5s.py
import tkinter as tk

def enable_button():
    btn.config(state="normal")

root = tk.Tk()
btn = tk.Button(root, text="Wait...", state="disabled")
btn.pack()
root.after(5000, enable_button)
root.mainloop()
