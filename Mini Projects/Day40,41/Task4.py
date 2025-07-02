import tkinter as tk
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def submit_form():
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    message = text_message.get("1.0", tk.END).strip()

    # Clear previous error message
    error_label.config(text="", fg="red")

    if not name:
        error_label.config(text="Name is required.")
    elif not is_valid_email(email):
        error_label.config(text="Invalid email format.")
    elif len(message) < 10:
        error_label.config(text="Message must be at least 10 characters.")
    else:
        error_label.config(text="Thank you for contacting us!", fg="green")
        # Optional: clear fields
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        text_message.delete("1.0", tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("Contact Form")
root.geometry("400x300")

# Labels and Entry widgets
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e", padx=10, pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Email:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
entry_email = tk.Entry(root, width=30)
entry_email.grid(row=1, column=1)

tk.Label(root, text="Message:").grid(row=2, column=0, sticky="ne", padx=10, pady=5)
text_message = tk.Text(root, width=30, height=5)
text_message.grid(row=2, column=1)

# Error/Success message label
error_label = tk.Label(root, text="", fg="red")
error_label.grid(row=3, columnspan=2, pady=10)

# Submit button
tk.Button(root, text="Submit", command=submit_form).grid(row=4, columnspan=2, pady=10)

root.mainloop()
