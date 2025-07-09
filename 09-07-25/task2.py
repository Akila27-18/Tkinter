# task2_checkbutton_disables_text.py
import tkinter as tk

def toggle_text_state():
    state = "disabled" if var.get() else "normal"
    text.config(state=state)

root = tk.Tk()
var = tk.BooleanVar()
check = tk.Checkbutton(root, text="Disable Text", variable=var, command=toggle_text_state)
check.pack()
text = tk.Entry(root)
text.pack()
root.mainloop()
