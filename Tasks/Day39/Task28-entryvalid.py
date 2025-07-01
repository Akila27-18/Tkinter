import tkinter as tk

def validate_input():
    value = entry.get()
    if value.isdigit():
        result_label.config(text=f"Valid number: {value}", fg="green")
    else:
        result_label.config(text="Please enter numbers only!", fg="red")

# GUI setup
root = tk.Tk()
root.title("Entry Validation Example")
root.geometry("300x150")

# Entry widget
tk.Label(root, text="Enter a number:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

# Validate button
tk.Button(root, text="Validate", command=validate_input).pack(pady=5)

# Result label
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()
