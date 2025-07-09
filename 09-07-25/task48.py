# task48_password_toggle.py
import tkinter as tk

class PasswordEntry(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.showing = False
        self.entry = tk.Entry(self, show="*")
        self.entry.pack(side="left")
        self.toggle_btn = tk.Button(self, text="Show", command=self.toggle)
        self.toggle_btn.pack(side="left")

    def toggle(self):
        self.showing = not self.showing
        self.entry.config(show="" if self.showing else "*")
        self.toggle_btn.config(text="Hide" if self.showing else "Show")

root = tk.Tk()
pwd_widget = PasswordEntry(root)
pwd_widget.pack(pady=20)
root.mainloop()
