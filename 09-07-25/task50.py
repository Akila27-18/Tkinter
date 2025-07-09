# task50_character_counter.py
import tkinter as tk

class CharCounter(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.var)
        self.entry.pack()
        self.count_label = tk.Label(self, text="Characters: 0")
        self.count_label.pack()
        self.var.trace_add("write", self.update_count)

    def update_count(self, *args):
        self.count_label.config(text=f"Characters: {len(self.var.get())}")

root = tk.Tk()
counter = CharCounter(root)
counter.pack(pady=20)
root.mainloop()
