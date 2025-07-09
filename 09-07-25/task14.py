# task14_radiobutton_disables_controls.py
import tkinter as tk

def toggle_controls():
    if option.get() == "Disable":
        entry.config(state="disabled")
    else:
        entry.config(state="normal")

root = tk.Tk()
option = tk.StringVar()
tk.Radiobutton(root, text="Enable Entry", value="Enable", variable=option, command=toggle_controls).pack()
tk.Radiobutton(root, text="Disable Entry", value="Disable", variable=option, command=toggle_controls).pack()
entry = tk.Entry(root)
entry.pack()
root.mainloop()
