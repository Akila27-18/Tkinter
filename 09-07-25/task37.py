# task37_entry_label_sync.py
import tkinter as tk

class LiveLabelEntry(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.var)
        self.label = tk.Label(self, text="")
        self.entry.pack()
        self.label.pack()
        self.var.trace_add("write", self.update_label)

    def update_label(self, *args):
        self.label.config(text=self.var.get())

root = tk.Tk()
widget = LiveLabelEntry(root)
widget.pack()
root.mainloop()
