import tkinter as tk

def toggle_button():
    if check_var.get():
        action_button.config(state="normal")  # Enable
    else:
        action_button.config(state="disabled")  # Disable

# Main window
root = tk.Tk()
root.title("Enable/Disable Button")
root.geometry("300x150")

# Checkbox variable
check_var = tk.BooleanVar()

# Checkbox
checkbox = tk.Checkbutton(root, text="Enable Button", variable=check_var, command=toggle_button)
checkbox.pack(pady=10)

# Button (initially disabled)
action_button = tk.Button(root, text="Click Me", state="disabled", command=lambda: print("Button Clicked!"))
action_button.pack(pady=10)

root.mainloop()
