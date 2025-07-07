import tkinter as tk
from tkinter import ttk
import re

# Email validation regex
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# Predefined list of courses
course_list = ["Python Basics", "Web Development", "Data Science", "AI & ML", "Cyber Security"]

# List to store enrolled students
enrollments = []

# Validate email format
def is_valid_email(email):
    return re.match(email_pattern, email)

# Enroll student function
def enroll_student():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    age = age_spinbox.get()
    course = course_combo.get()

    if not name or not email or not age or not course:
        status_label.config(text="All fields are required!", fg="red")
    elif not is_valid_email(email):
        status_label.config(text="Invalid email format", fg="red")
    else:
        entry = f"{name} ({age}) - {course} | {email}"
        enrolled_listbox.insert(tk.END, entry)
        enrollments.append(entry)
        status_label.config(text="Student enrolled successfully!", fg="green")
        clear_inputs()

def clear_inputs():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    age_spinbox.delete(0, tk.END)
    age_spinbox.insert(0, "18")
    course_combo.set("")

# Main window
root = tk.Tk()
root.title("Student Course Enrollment App")
root.geometry("600x400")

# ========== Input Frame ==========
input_frame = tk.LabelFrame(root, text="Student Registration", padx=10, pady=10)
input_frame.pack(padx=20, pady=10, fill="x")

tk.Label(input_frame, text="Name:").grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(input_frame, width=30)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(input_frame, text="Email:").grid(row=1, column=0, sticky="e")
email_entry = tk.Entry(input_frame, width=30)
email_entry.grid(row=1, column=1, pady=5)

tk.Label(input_frame, text="Age:").grid(row=2, column=0, sticky="e")
age_spinbox = tk.Spinbox(input_frame, from_=10, to=100, width=5)
age_spinbox.grid(row=2, column=1, sticky="w")
age_spinbox.delete(0, tk.END)
age_spinbox.insert(0, "18")

tk.Label(input_frame, text="Course:").grid(row=3, column=0, sticky="e")
course_combo = ttk.Combobox(input_frame, values=course_list, state="readonly", width=27)
course_combo.grid(row=3, column=1, pady=5)

enroll_button = tk.Button(input_frame, text="Enroll", command=enroll_student)
enroll_button.grid(row=4, column=0, columnspan=2, pady=10)

status_label = tk.Label(input_frame, text="", fg="green")
status_label.grid(row=5, column=0, columnspan=2)

# ========== Enrolled Students Frame ==========
list_frame = tk.LabelFrame(root, text="Enrolled Students", padx=10, pady=10)
list_frame.pack(padx=20, pady=10, fill="both", expand=True)

# Listbox + Scrollbar
enrolled_listbox = tk.Listbox(list_frame, height=10)
enrolled_listbox.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

enrolled_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=enrolled_listbox.yview)

root.mainloop()
