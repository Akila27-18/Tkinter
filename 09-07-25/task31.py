# task31_keyrelease_shift.py
import tkinter as tk

def key_release(event):
    if event.keysym == "Shift_L" or event.keysym == "Shift_R":
        print("Shift key released")

root = tk.Tk()
root.bind("<KeyRelease>", key_release)
root.mainloop()
