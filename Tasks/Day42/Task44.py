import tkinter as tk

def update_label(*args):
    label.config(text=f"Value: {spin_value.get()}")

root = tk.Tk()
root.title("Dynamic Spinbox Value")

# StringVar to track Spinbox value
spin_value = tk.StringVar()
spin_value.trace_add("write", update_label)

# Create Spinbox
spinbox = tk.Spinbox(root, from_=0, to=100, textvariable=spin_value)
spinbox.pack(pady=10)

# Label to display value
label = tk.Label(root, text="Value: 0")
label.pack(pady=5)

root.mainloop()
