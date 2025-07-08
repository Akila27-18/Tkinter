import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Data structure to store shift assignments
shift_schedule = {}

# Assign selected shift
def assign_shift():
    selected = employee_listbox.curselection()
    if not selected:
        log_var.set("Select an employee.")
        return

    employee = employee_listbox.get(selected[0])
    shift = shift_var.get()
    time = time_var.get()

    if not shift or not time:
        log_var.set("Select shift and time.")
        return

    shift_schedule[employee] = f"{shift} ({time})"
    log_var.set(f"Assigned {employee} to {shift} ({time})")

# Clear all assignments
def clear_schedule():
    shift_schedule.clear()
    log_var.set("Schedule cleared.")

# Export schedule
def export_schedule():
    if not shift_schedule:
        messagebox.showwarning("No Data", "No schedule to export.")
        return

    confirm = messagebox.askyesno("Confirm Export", "Do you want to export the schedule?")
    if confirm:
        filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text Files", "*.txt")])
        if filepath:
            try:
                with open(filepath, "w") as file:
                    for emp, shift in shift_schedule.items():
                        file.write(f"{emp}: {shift}\n")
                messagebox.showinfo("Exported", f"Schedule exported to:\n{filepath}")
            except Exception as e:
                messagebox.showerror("Error", f"Export failed:\n{e}")

# Main Window
root = tk.Tk()
root.title("Employee Shift Scheduler")
root.geometry("600x400")

# ---------------- Menu ----------------
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Export Schedule", command=export_schedule)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)

# ---------------- Toolbar ----------------
toolbar = tk.Frame(root)
toolbar.pack(fill='x', padx=10, pady=5)

tk.Button(toolbar, text="Assign", command=assign_shift).pack(side='left', padx=5)
tk.Button(toolbar, text="Clear", command=clear_schedule).pack(side='left', padx=5)

# ---------------- Frames ----------------
main_frame = tk.Frame(root)
main_frame.pack(fill='both', expand=True, padx=10, pady=5)

# Frame 1: Employee List
frame1 = tk.LabelFrame(main_frame, text="Employees", padx=10, pady=10)
frame1.pack(side='left', fill='both', expand=True)

employee_listbox = tk.Listbox(frame1, height=15)
employees = ["Alice", "Bob", "Charlie", "David", "Eva"]
for emp in employees:
    employee_listbox.insert(tk.END, emp)
employee_listbox.pack(fill='both', expand=True)

# Frame 2: Shift Assignment Controls
frame2 = tk.LabelFrame(main_frame, text="Assign Shift", padx=10, pady=10)
frame2.pack(side='right', fill='both', expand=True)

tk.Label(frame2, text="Shift").grid(row=0, column=0, sticky='w')
shift_var = tk.StringVar()
ttk.Combobox(frame2, textvariable=shift_var,
             values=["Morning", "Afternoon", "Night"]).grid(row=0, column=1)

tk.Label(frame2, text="Time").grid(row=1, column=0, sticky='w')
time_var = tk.StringVar()
tk.Entry(frame2, textvariable=time_var).grid(row=1, column=1)

# Log display
log_var = tk.StringVar()
tk.Label(root, textvariable=log_var, fg="blue", anchor="w").pack(fill='x', padx=10, pady=5)

root.mainloop()
