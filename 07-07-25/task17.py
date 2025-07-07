import tkinter as tk
from tkinter import ttk, messagebox
import re

# Validate email using regex
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def confirm_booking():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    destination = destination_combo.get()
    travelers = travelers_spinbox.get()

    # Validation
    if not name:
        messagebox.showerror("Input Error", "Please enter your name.")
        return
    if not email or not is_valid_email(email):
        messagebox.showerror("Input Error", "Please enter a valid email address.")
        return
    if destination == "":
        messagebox.showerror("Input Error", "Please select a destination.")
        return

    # Output confirmation
    confirmation = f"Booking Confirmed!\n\nName: {name}\nEmail: {email}\nDestination: {destination}\nTravelers: {travelers}"
    confirmation_label.config(text=confirmation)

# Main window
root = tk.Tk()
root.title("Travel Booking")
root.geometry("450x400")
root.resizable(False, False)

# Labels and Inputs
tk.Label(root, text="Name:").place(x=30, y=30)
name_entry = tk.Entry(root, width=30)
name_entry.place(x=150, y=30)

tk.Label(root, text="Email:").place(x=30, y=80)
email_entry = tk.Entry(root, width=30)
email_entry.place(x=150, y=80)

tk.Label(root, text="Destination:").place(x=30, y=130)
destination_combo = ttk.Combobox(root, values=["Paris", "New York", "Tokyo", "London", "Dubai"], state="readonly", width=27)
destination_combo.place(x=150, y=130)

tk.Label(root, text="Number of Travelers:").place(x=30, y=180)
travelers_spinbox = tk.Spinbox(root, from_=1, to=20, width=5)
travelers_spinbox.place(x=190, y=180)

# Confirm Button
confirm_btn = tk.Button(root, text="Confirm Booking", command=confirm_booking, bg="lightblue")
confirm_btn.place(x=160, y=230)

# Confirmation Label
confirmation_label = tk.Label(root, text="", justify="left", fg="green", font=("Arial", 10), wraplength=400)
confirmation_label.place(x=30, y=280)

root.mainloop()
