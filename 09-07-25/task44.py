# task44_toolbar.py
import tkinter as tk

class Toolbar(tk.Frame):
    def __init__(self, master, actions, **kwargs):
        super().__init__(master, **kwargs)
        for label, callback in actions.items():
            tk.Button(self, text=label, command=callback).pack(side="left", padx=5)

root = tk.Tk()
actions = {
    "Open": lambda: print("Open clicked"),
    "Save": lambda: print("Save clicked"),
    "Exit": root.destroy
}
widget = Toolbar(root, actions)
widget.pack(fill="x", pady=10)
root.mainloop()
