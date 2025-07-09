# task4_checkbox_enables_submit.py
import tkinter as tk

def toggle_submit():
    submit_btn.config(state="normal" if agree_var.get() else "disabled")

root = tk.Tk()
agree_var = tk.BooleanVar()
check = tk.Checkbutton(root, text="I Agree", variable=agree_var, command=toggle_submit)
check.pack()
submit_btn = tk.Button(root, text="Submit", state="disabled")
submit_btn.pack()
root.mainloop()
