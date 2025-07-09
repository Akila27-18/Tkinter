# task9_combobox_toggle.py
import tkinter as tk
from tkinter.ttk import Combobox

def toggle_state(event):
    val = combo.get()
    btn.config(state="normal" if val == "Enable" else "disabled")

root = tk.Tk()
combo = Combobox(root, values=["Enable", "Disable"])
combo.bind("<<ComboboxSelected>>", toggle_state)
combo.pack()
btn = tk.Button(root, text="Action")
btn.pack()
root.mainloop()
