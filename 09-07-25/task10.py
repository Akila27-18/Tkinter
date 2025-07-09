# task10_disable_group_buttons.py
import tkinter as tk

def disable_all():
    for btn in buttons:
        btn.config(state="disabled")

root = tk.Tk()
buttons = [tk.Button(root, text=f"Button {i}") for i in range(3)]
for b in buttons: b.pack()
tk.Button(root, text="Disable All", command=disable_all).pack()
root.mainloop()
