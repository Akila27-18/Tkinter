import tkinter as tk
from tkinter import messagebox

# Sample student list
students = [f"Student {i+1}" for i in range(30)]  # Change or load dynamically

# Dictionary to track attendance status
attendance_status = {}  # student_name -> "Present"/"Absent"

def mark_attendance(status):
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("No Selection", "Please select a student.")
        return
    for i in selected:
        name = listbox.get(i)
        attendance_status[name] = status
        color = "green" if status == "Present" else "red"
        listbox.itemconfig(i, {'bg': color, 'fg': 'white'})
    update_summary()

def update_summary():
    present = sum(1 for s in attendance_status.values() if s == "Present")
    absent = sum(1 for s in attendance_status.values() if s == "Absent")
    summary_label.config(text=f"Present: {present}   Absent: {absent}")

# Main window
root = tk.Tk()
root.title("Attendance Tracker")
root.geometry("400x400")

# Listbox with scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, width=30, height=15, selectmode=tk.MULTIPLE, yscrollcommand=scrollbar.set)
for student in students:
    listbox.insert(tk.END, student)
listbox.pack(side=tk.LEFT)
scrollbar.config(command=listbox.yview)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Mark Present", bg="green", fg="white", width=15,
          command=lambda: mark_attendance("Present")).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Mark Absent", bg="red", fg="white", width=15,
          command=lambda: mark_attendance("Absent")).grid(row=0, column=1, padx=5)

# Summary label
summary_label = tk.Label(root, text="Present: 0   Absent: 0", font=("Arial", 12, "bold"))
summary_label.pack(pady=10)

root.mainloop()
