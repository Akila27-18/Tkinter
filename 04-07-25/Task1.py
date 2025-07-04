import tkinter as tk
from tkinter import messagebox
import re

# Email validation using regex
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
    return re.match(pattern, email)

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    age = spinbox_age.get()
    about = text_about.get("1.0", tk.END).strip()

    if not name or not email or not phone:
        messagebox.showwarning("Missing Info", "Please fill in all required fields.")
        return

    if not is_valid_email(email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        return

    output = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nAge: {age}\nAbout: {about}"
    label_output.config(text=output)

# Root window
root = tk.Tk()
root.title("Personal Information Form")
root.geometry("450x500")
root.resizable(False, False)

# Personal Details Frame
frame_personal = tk.LabelFrame(root, text="Personal Details", padx=10, pady=10)
frame_personal.pack(padx=10, pady=10, fill="both")

# Name
tk.Label(frame_personal, text="Name:").grid(row=0, column=0, sticky="e")
entry_name = tk.Entry(frame_personal, width=30)
entry_name.grid(row=0, column=1, pady=5)

# Email
tk.Label(frame_personal, text="Email:").grid(row=1, column=0, sticky="e")
entry_email = tk.Entry(frame_personal, width=30)
entry_email.grid(row=1, column=1, pady=5)

# Phone
tk.Label(frame_personal, text="Phone:").grid(row=2, column=0, sticky="e")
entry_phone = tk.Entry(frame_personal, width=30)
entry_phone.grid(row=2, column=1, pady=5)

# Age
tk.Label(frame_personal, text="Age:").grid(row=3, column=0, sticky="e")
spinbox_age = tk.Spinbox(frame_personal, from_=10, to=100, width=5)
spinbox_age.grid(row=3, column=1, sticky="w", pady=5)

# About You Frame
frame_about = tk.LabelFrame(root, text="About You", padx=10, pady=10)
frame_about.pack(padx=10, pady=10, fill="both")

text_about = tk.Text(frame_about, height=5, width=40)
text_about.pack()

# Submit Button
btn_submit = tk.Button(root, text="Submit", command=submit_form, bg="#4CAF50", fg="white")
btn_submit.pack(pady=10)

# Output Label
label_output = tk.Label(root, text="", justify="left", anchor="w", bg="white", width=60, height=10, relief="sunken", wraplength=400)
label_output.pack(padx=10, pady=10)

root.mainloop()
