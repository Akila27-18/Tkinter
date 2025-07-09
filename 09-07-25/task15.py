# task15_toggle_multiple_controls.py
import tkinter as tk

def toggle_all():
    state = "normal" if entry['state'] == "disabled" else "disabled"
    entry.config(state=state)
    btn.config(state=state)
    lbl.config(state=state)

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
btn = tk.Button(root, text="Press")
btn.pack()
lbl = tk.Label(root, text="Status")
lbl.pack()
tk.Button(root, text="Toggle All", command=toggle_all).pack()
root.mainloop()
