# task12_visual_state_change.py
import tkinter as tk

def toggle_state():
    if btn['state'] == 'normal':
        btn.config(state="disabled", bg="gray", fg="white")
    else:
        btn.config(state="normal", bg="green", fg="black")

root = tk.Tk()
btn = tk.Button(root, text="Toggle Me", bg="green", command=toggle_state)
btn.pack()
root.mainloop()
