import tkinter as tk
from tkinter import messagebox
import re

# Validate email using regex
def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

def update_info():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    bio = bio_text.get("1.0", tk.END).strip()

    # Validations
    if not name:
        messagebox.showerror("Validation Error", "Name cannot be empty.")
        return
    if not email or not is_valid_email(email):
        messagebox.showerror("Validation Error", "Invalid email address.")
        return
    if len(bio) < 10:
        messagebox.showerror("Validation Error", "Bio should be at least 10 characters.")
        return

    # Update labels
    name_display.config(text=name)
    email_display.config(text=email)
    bio_display.config(text=bio)

# Main Window
root = tk.Tk()
root.geometry("600x400")
root.title("Personal Portfolio Dashboard")
root.iconbitmap("favicon.ico")  # Replace with a valid .ico file path

# Labels
tk.Label(root, text="Enter Your Name:").place(x=30, y=30)
tk.Label(root, text="Enter Your Email:").place(x=30, y=80)
tk.Label(root, text="Enter Your Bio:").place(x=30, y=130)

# Entry Widgets
name_entry = tk.Entry(root, width=30)
name_entry.place(x=160, y=30)

email_entry = tk.Entry(root, width=30)
email_entry.place(x=160, y=80)

bio_text = tk.Text(root, width=40, height=4)
bio_text.place(x=160, y=130)

# Update Button
update_btn = tk.Button(root, text="Update Info", command=update_info, bg="lightblue")
update_btn.place(x=250, y=200)

# Display Section
tk.Label(root, text="Your Name:", font=("Arial", 10, "bold")).place(x=30, y=250)
name_display = tk.Label(root, text="", fg="blue")
name_display.place(x=160, y=250)

tk.Label(root, text="Your Email:", font=("Arial", 10, "bold")).place(x=30, y=280)
email_display = tk.Label(root, text="", fg="blue")
email_display.place(x=160, y=280)

tk.Label(root, text="Your Bio:", font=("Arial", 10, "bold")).place(x=30, y=310)
bio_display = tk.Label(root, text="", fg="blue", justify="left", wraplength=350)
bio_display.place(x=160, y=310)

root.mainloop()
