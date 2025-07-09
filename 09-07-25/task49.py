# task49_progress_label_fill.py
import tkinter as tk

class ProgressTracker(tk.Frame):
    def __init__(self, master, word="PROGRESS", **kwargs):
        super().__init__(master, **kwargs)
        self.word = word
        self.index = 0
        self.label = tk.Label(self, text="_" * len(word), font=("Courier", 16))
        self.label.pack()
        self.button = tk.Button(self, text="Next Step", command=self.next)
        self.button.pack(pady=5)

    def next(self):
        if self.index < len(self.word):
            updated = self.word[:self.index+1] + "_" * (len(self.word) - self.index - 1)
            self.label.config(text=updated)
            self.index += 1

root = tk.Tk()
tracker = ProgressTracker(root)
tracker.pack(pady=20)
root.mainloop()
