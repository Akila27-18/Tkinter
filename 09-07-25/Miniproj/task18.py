import tkinter as tk
from tkinter import messagebox

# Tooltip creation function
def create_tooltip(widget, text):
    tooltip = None

    def on_enter(event):
        nonlocal tooltip
        x = event.x_root + 10
        y = event.y_root + 10
        tooltip = tk.Toplevel(widget)
        tooltip.overrideredirect(True)  # No window decorations
        tooltip.geometry(f"+{x}+{y}")
        label = tk.Label(tooltip, text=text, bg="lightyellow", relief="solid",
                         borderwidth=1, font=("Arial", 10))
        label.pack()

    def on_leave(event):
        nonlocal tooltip
        if tooltip:
            tooltip.destroy()
            tooltip = None

    widget.bind("<Enter>", on_enter)
    widget.bind("<Leave>", on_leave)

# Submit button action
def submit_action():
    name = entry.get().strip()
    if name:
        messagebox.showinfo("Submitted", f"Hello {name}, form submitted!")
    else:
        messagebox.showwarning("Missing Info", "Please enter your name.")

# Main UI
root = tk.Tk()
root.title("Hover Tooltip Example")
root.geometry("300x200")

# Entry field
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=20)
create_tooltip(entry, "Enter your name here.")

# Submit button
btn1 = tk.Button(root, text="Submit", command=submit_action)
btn1.pack(pady=10)
create_tooltip(btn1, "Click to submit the form.")

root.mainloop()
