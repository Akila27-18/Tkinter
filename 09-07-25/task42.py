# task42_rating_bar.py
import tkinter as tk

class StarRating(tk.Frame):
    def __init__(self, master, total=5, **kwargs):
        super().__init__(master, **kwargs)
        self.stars = []
        self.rating = tk.IntVar(value=0)
        for i in range(1, total+1):
            b = tk.Button(self, text="☆", command=lambda i=i: self.set_rating(i))
            b.pack(side="left")
            self.stars.append(b)

    def set_rating(self, value):
        self.rating.set(value)
        for i, b in enumerate(self.stars):
            b.config(text="★" if i < value else "☆")

root = tk.Tk()
widget = StarRating(root)
widget.pack(pady=10)
root.mainloop()
