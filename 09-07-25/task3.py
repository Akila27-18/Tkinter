# task3_disable_other_button.py
import tkinter as tk

def disable_other():
    btn2.config(state="disabled")

root = tk.Tk()
btn1 = tk.Button(root, text="Disable Button 2", command=disable_other)
btn1.pack()
btn2 = tk.Button(root, text="Button 2")
btn2.pack()
root.mainloop()
