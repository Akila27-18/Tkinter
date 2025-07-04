import tkinter as tk

def toggle_spinbox():
    if check_var.get():
        spinbox.config(state="disabled")
    else:
        spinbox.config(state="normal")

root = tk.Tk()
root.title("Conditional Spinbox Disable")
root.geometry("250x150")

# Spinbox widget
spinbox = tk.Spinbox(root, from_=0, to=100)
spinbox.pack(pady=10)

# Checkbox to disable/enable Spinbox
check_var = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Disable Spinbox", variable=check_var, command=toggle_spinbox)
checkbox.pack()

root.mainloop()
