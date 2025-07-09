# task8_button_active_state.py
import tkinter as tk

root = tk.Tk()
btn = tk.Button(root, text="Hover Me", activebackground="lightgreen", activeforeground="blue")
btn.pack()
root.mainloop()
