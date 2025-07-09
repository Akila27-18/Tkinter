# task38_ok_cancel_widget.py
import tkinter as tk

class OkCancel(tk.Frame):
    def __init__(self, master, on_ok, on_cancel, **kwargs):
        super().__init__(master, **kwargs)
        tk.Button(self, text="OK", command=on_ok).pack(side="left", padx=5)
        tk.Button(self, text="Cancel", command=on_cancel).pack(side="right", padx=5)

def ok(): print("OK clicked")
def cancel(): print("Cancel clicked")

root = tk.Tk()
widget = OkCancel(root, on_ok=ok, on_cancel=cancel)
widget.pack(pady=10)
root.mainloop()
