import tkinter as tk
import re

# Regex for email validation
EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# Validation function
def validate_email():
    email = email_entry.get().strip()
    if re.match(EMAIL_REGEX, email):
        result_label.config(text="Valid Email", fg="green")
    else:
        result_label.config(text="Invalid Email", fg="red")

# Main window
root = tk.Tk()
root.title("Email Validator")
root.geometry("400x200")

# Label and Entry for Email
tk.Label(root, text="Enter Email:", font=("Arial", 12)).place(x=30, y=40)
email_entry = tk.Entry(root, width=30, font=("Arial", 12))
email_entry.place(x=140, y=40)

# Validate Button
validate_btn = tk.Button(root, text="Validate", command=validate_email)
validate_btn.place(x=160, y=80)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.place(x=140, y=130)

# Run the app
root.mainloop()
