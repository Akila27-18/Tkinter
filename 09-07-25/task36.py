# task36_label_button_widget.py
import tkinter as tk

class LabelButton(tk.Frame):
    def __init__(self, master, text, button_text, **kwargs):
        super().__init__(master, **kwargs)
        self.label = tk.Label(self, text=text)
        self.label.pack(side="left")
        self.button = tk.Button(self, text=button_text)
        self.button.pack(side="right")

root = tk.Tk()
widget = LabelButton(root, "Greeting:", "Say Hi")
widget.pack(pady=10)
root.mainloop()
