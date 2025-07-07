import tkinter as tk
from tkinter import ttk

# Sample student list
students = [
    f"Student {i+1}" for i in range(30)
]

# Track attendance
attendance_status = {}

def update_listbox():
    listbox.delete(0, tk.END)
    for name in students:
        status = attendance_status.get(name, "")
        display_text = name
        if status == "Present":
            display_text = "✅ " + name
        elif status == "Absent":
            display_text = "❌ " + name
        listbox.insert(tk.END, display_text)

        # Optional: Set color
        index = listbox.size() - 1
        if status == "Present":
            listbox.itemconfig(index, {'fg': 'green'})
        elif status == "Absent":
            listbox.itemconfig(index, {'fg': 'red'})

def mark_attendance(mark_type):
    selected = listbox.curselection()
    if not selected:
        return
    index = selected[0]
    original_name = students[index]
    attendance_status[original_name] = mark_type
    update_listbox()

# Main window
root = tk.Tk()
root.title("Student Attendance Marker")
root.geometry("300x400")

# Frame for Listbox + Scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

# Listbox and Scrollbar
scrollbar = tk.Scrollbar(frame)
listbox = tk.Listbox(frame, width=30, height=15, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Populate listbox initially
update_listbox()

# Buttons
btn_present = ttk.Button(root, text="Mark Present", command=lambda: mark_attendance("Present"))
btn_absent = ttk.Button(root, text="Mark Absent", command=lambda: mark_attendance("Absent"))
btn_present.pack(pady=5)
btn_absent.pack(pady=5)

# Run the app
root.mainloop()
