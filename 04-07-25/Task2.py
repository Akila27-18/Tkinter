import tkinter as tk
from tkinter import ttk, messagebox

# Sample courses
COURSES = ["Computer Science", "Mathematics", "Physics", "Biology", "English"]

def register_student():
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    course = combo_course.get().strip()
    age = spin_age.get()

    # Simple validation
    if not name or not email or not course:
        messagebox.showwarning("Validation Error", "All fields are required.")
        return
    if "@" not in email or "." not in email:
        messagebox.showwarning("Validation Error", "Invalid email address.")
        return

    # Format and insert student info
    student_info = f"{name} | {email} | {course} | Age: {age}"
    listbox_students.insert(tk.END, student_info)

    # Clear fields
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    combo_course.set('')
    spin_age.delete(0, tk.END)
    spin_age.insert(0, 18)

# Main Window
root = tk.Tk()
root.title("Student Registration App")
root.geometry("500x400")

# --- Top Frame (Form) ---
frame_top = tk.Frame(root, pady=10)
frame_top.pack()

# Name
tk.Label(frame_top, text="Name:").pack(anchor="w")
entry_name = tk.Entry(frame_top, width=40)
entry_name.pack()

# Email
tk.Label(frame_top, text="Email:").pack(anchor="w")
entry_email = tk.Entry(frame_top, width=40)
entry_email.pack()

# Course
tk.Label(frame_top, text="Course:").pack(anchor="w")
combo_course = ttk.Combobox(frame_top, values=COURSES, state="readonly", width=37)
combo_course.pack()

# Age
tk.Label(frame_top, text="Age:").pack(anchor="w")
spin_age = tk.Spinbox(frame_top, from_=17, to=30, width=5)
spin_age.pack()

# Submit Button
btn_submit = tk.Button(frame_top, text="Register", command=register_student, bg="green", fg="white")
btn_submit.pack(pady=5)

# --- Bottom Frame (Listbox with Scrollbar) ---
frame_bottom = tk.Frame(root)
frame_bottom.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Scrollbar
scrollbar = tk.Scrollbar(frame_bottom)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Listbox
listbox_students = tk.Listbox(frame_bottom, yscrollcommand=scrollbar.set, width=70, height=10)
listbox_students.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox_students.yview)

root.mainloop()
