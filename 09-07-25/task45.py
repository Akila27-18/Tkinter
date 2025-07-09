# task45_labeled_entry.py
import tkinter as tk

class LabeledEntry(tk.Frame):
    def __init__(self, master, label_text, **kwargs):
        super().__init__(master, **kwargs)
        tk.Label(self, text=label_text, font=("Arial", 10, "bold")).pack(side="left", padx=5)
        self.entry = tk.Entry(self, bg="#f0f0ff", font=("Arial", 10))
        self.entry.pack(side="left")

root = tk.Tk()
widget = LabeledEntry(root, "Name:")
widget.pack(pady=10)
root.mainloop()
