import tkinter as tk
from tkinter import ttk, messagebox
import re

def validate_name(name):
    return name and re.match(r'^[A-Za-z ]+$', name)

def validate_email(email):
    return email and re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

def validate_phone(phone):
    return phone and re.match(r'^\d{10}$', phone)

def submit_form():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()
    age = age_spinbox.get()
    course = course_combobox.get()

    # Validations
    if not validate_name(name):
        msg_label.config(text="Invalid name! Use only letters and spaces.", fg="red")
        return

    if not validate_email(email):
        msg_label.config(text="Invalid email format!", fg="red")
        return

    if not validate_phone(phone):
        msg_label.config(text="Phone must be 10 digits!", fg="red")
        return

    try:
        age_int = int(age)
        if age_int < 15 or age_int > 60:
            raise ValueError
    except ValueError:
        msg_label.config(text="Age must be between 15 and 60.", fg="red")
        return

    if not course:
        msg_label.config(text="Please select a course.", fg="red")
        return

    # All validations passed
    entry = f"{name}, {email}, {phone}, Age: {age}, Course: {course}"
    student_listbox.insert(tk.END, entry)
    msg_label.config(text="Student registered successfully!", fg="green")

    # Clear fields
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    age_spinbox.delete(0, tk.END)
    age_spinbox.insert(0, "18")
    course_combobox.set("")

# === GUI Setup ===
root = tk.Tk()
root.title("Student Registration System")
root.geometry("620x430")
root.resizable(False, False)

# ==== Frame ====
form_frame = tk.Frame(root, padx=20, pady=20)
form_frame.pack()

# ==== Form Inputs ====
tk.Label(form_frame, text="Name:").grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1)

tk.Label(form_frame, text="Email:").grid(row=1, column=0, sticky="e")
email_entry = tk.Entry(form_frame, width=30)
email_entry.grid(row=1, column=1)

tk.Label(form_frame, text="Phone:").grid(row=2, column=0, sticky="e")
phone_entry = tk.Entry(form_frame, width=30)
phone_entry.grid(row=2, column=1)

tk.Label(form_frame, text="Age:").grid(row=3, column=0, sticky="e")
age_spinbox = tk.Spinbox(form_frame, from_=15, to=60, width=5)
age_spinbox.grid(row=3, column=1, sticky="w")
age_spinbox.delete(0, tk.END)
age_spinbox.insert(0, "18")

tk.Label(form_frame, text="Course:").grid(row=4, column=0, sticky="e")
course_combobox = ttk.Combobox(
    form_frame,
    values=["Python", "Java", "C++", "Web Dev", "Data Science"],
    state="readonly",
    width=27
)
course_combobox.grid(row=4, column=1)

# ==== Submit Button ====
submit_btn = tk.Button(form_frame, text="Submit", command=submit_form, width=20, bg="blue", fg="white")
submit_btn.grid(row=5, column=0, columnspan=2, pady=10)

# ==== Confirmation Message ====
msg_label = tk.Label(root, text="", font=("Arial", 10))
msg_label.pack()

# ==== Listbox with Scrollbar ====
list_frame = tk.Frame(root)
list_frame.pack(pady=10)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

student_listbox = tk.Listbox(list_frame, width=85, height=8, yscrollcommand=scrollbar.set)
student_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=student_listbox.yview)

root.mainloop()
