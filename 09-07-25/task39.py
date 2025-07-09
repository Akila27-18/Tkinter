# task39_searchbox_widget.py
import tkinter as tk

class SearchBox(tk.Frame):
    def __init__(self, master, on_search, **kwargs):
        super().__init__(master, **kwargs)
        self.entry = tk.Entry(self)
        self.entry.pack(side="left", fill="x", expand=True)
        tk.Button(self, text="Search", command=lambda: on_search(self.entry.get())).pack(side="right")

def search(term): print(f"Searching for: {term}")

root = tk.Tk()
widget = SearchBox(root, on_search=search)
widget.pack(fill="x", padx=10, pady=10)
root.mainloop()
