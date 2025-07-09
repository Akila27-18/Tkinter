# task26_keypress_log.py
import tkinter as tk

def log_key(event):
    print(f"Key pressed: {event.char} (KeyCode: {event.keycode})")

root = tk.Tk()
root.bind("<KeyPress>", log_key)
root.mainloop()
